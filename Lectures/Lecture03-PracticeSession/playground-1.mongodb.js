/* global use, db */
// MongoDB Playground
// To disable this template go to Settings | MongoDB | Use Default Template For Playground.
// Make sure you are connected to enable completions and to be able to run a playground.
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.
// The result of the last command run in a playground is shown on the results panel.
// By default the first 20 documents will be returned with a cursor.
// Use 'console.log()' to print to the debug output.
// For more documentation on playgrounds please refer to
// https://www.mongodb.com/docs/mongodb-vscode/playgrounds/

// Select the database to use.
use('abcdef');

// db.students.insertMany([
//     {
//         name: "Ali",
//         course: "Web Development",
//         marks: 85,
//         city: "Karachi",
//         gender: "Male"
//     },
//     {
//         name: "Ahmed",
//         course: "Web Development",
//         marks: 72,
//         city: "Lahore",
//         gender: "Male"
//     },
//     {
//         name: "Sara",
//         course: "Data Science",
//         marks: 91,
//         city: "Karachi",
//         gender: "Female"
//     },
//     {
//         name: "Ayesha",
//         course: "Data Science",
//         marks: 78,
//         city: "Islamabad",
//         gender: "Female"
//     },
//     {
//         name: "Usman",
//         course: "Web Development",
//         marks: 65,
//         city: "Karachi",
//         gender: "Male"
//     }
// ]);

db.students.find();

// Match Stage
db.students.aggregate([
  {
    $match: {
      city: "Karachi",
      marks: { $gt: 70 }
    }
  }
])

// Project Stage ( with _id )
db.students.aggregate([
  {
    $project: {
      city: 1, 
      marks: 1
    }
  }
])

// Project Stage ( without _id )
db.students.aggregate([
  {
    $project: {
      _id: 0,
      city: 1, 
      marks: 1
    }
  }
])

// Match & Project Stages Combined
db.students.aggregate([
  {
    $match: {
      city: "Karachi"
    }
  },
  {
    $project: {
      _id: 0, 
      name: 1, 
      marks: 1
    }
  }
])


// Sort Stage 
db.students.aggregate([
  {
    $sort: {
      marks: 1
    }
  }
])

// Sort Stage with Limit Stage
db.students.aggregate([
  {
    $sort: {
      marks: 1
    }
  }, 
  {
    $limit: 3
  }
])

// Group Stage
db.students.aggregate([
  {
    $group: {
      _id: "$course"
    } 
  }
])


// $group + $sum => Sum is behaving as count here!
db.students.aggregate([
  {
    $group: {
      _id: "$course", 
      totalStudents: {
        $sum: 1
      }
    }
  }
])

// $group + avg
db.students.aggregate([
  {
    $group: {
      _id: "$course", 
      averageMarks: {
        $avg: "$marks"
      }
    }
  }
])

// $group + $sum + $avg + $max + $min
db.students.aggregate([
  {
    $group: {
      _id: "$course", 
      totalStudents: {
        $sum: 1
      }, 
      averageMarks: {
        $avg: "$marks"
      }, 
      highestMarks: {
        $max: "$marks"
      }, 
      lowestMarks: {
        $min: "$marks"
      }
    }
  }
])

// $group with $sort
db.students.aggregate([
  {
    $group: {
      _id: "$course", 
      totalStudents: {
        $sum: 1
      }, 
      averageMarks: {
        $avg: "$marks"
      }, 
      highestMarks: {
        $max: "$marks"
      }, 
      lowestMarks: {
        $min: "$marks"
      }
    }
  }, 

  {
    $sort: {
      averageMarks: -1
    }
  }
])

// $skip 
db.students.aggregate([
  {
    $sort: {
      marks: -1
    }
  }, 
  {
    $skip: 2
  }
])

// $skip + $limit => Common combination for pagination
db.students.aggregate([
  {
    $sort: {
      marks: -1
    }
  },
  {
    $skip: 2
  }, 
  {
    $limit: 2
  }
])


// LEVEL 2: DATA TRANSFORMATION
// $set with $add => Temporary result of aggregation as 'finalMarks' field have been shown in result ( Not saved permanently in database )
db.students.aggregate([
  {
    $set: {
      finalMarks: {
        $add: ["$marks", 5]
      }
    }
  }
])

// Multiple Calculations
db.students.aggregate([
  {
    $set: {
      finalMarks: {
        $add: ["$marks", 5]
      }, 

      marksAfterBonus: {
        $round: [ { $multiply: ["$marks", 1.1] }, 2 ]
      },

      halfMarks: {
        $divide: ["$marks", 2]
      }
    }
  }
])

// Percentage
db.students.aggregate([
 {
   $set: {
    percentage: {
      $round: [
        {
          $multiply: [ 
        {
          $divide: ["$marks", 300]
        }, 100
      ]
        }, 1
      ]
    }
  }
 }
])

// $set + $project
db.students.aggregate([
  {
    $set: {
      finalMarks: {
        $add: ["$marks", 5]
      }, 
      percentage: {
        $round: [
          {
            $multiply: [
              {
                $divide: ["$marks", 100]
              }, 100
            ]
          }, 2
        ]
      }
    }
  },
  {
    $project: {
      _id: 0, 
      name: 1, 
      marks: 1, 
      finalMarks: 1, 
      percentage: 1
    }
  }
])