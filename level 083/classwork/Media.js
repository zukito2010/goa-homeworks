function sum(arr) {
    return arr.reduce(function (a, b) {
       return a + b;
    }, 0);
 }
 
 class Media {
   constructor(title, ratings = []) {
     this._title = title;
     this._isCheckedOut = false;
     this._ratings = ratings;
   }
 
   get title() {
     return this._title;
   }
 
   get isCheckedOut() {
     return this._isCheckedOut;
   }
 
   set isCheckedOut(isIt) {
     this._isCheckedOut = isIt;
   }
 
   get ratings() {
     return this._ratings;
   }
 
   toggleCheckOutStatus() {
     this._isCheckedOut = !this._isCheckedOut;
   }
 
   getAverageRating() {
     return this._ratings.length > 0 ? sum(this._ratings) / this._ratings.length : 0;
   }
 
   addRating(rating) {
     if (rating >= 1 && rating <= 5) {
       this._ratings.push(rating);
     }
   }
 }
 
 class Book extends Media {
   constructor(title, author, pages, ratings = []) {
     super(title, ratings);
     this._author = author;
     this._pages = pages;
   }
 
   get author() {
     return this._author;
   }
 
   get pages() {
     return this._pages;
   }
 }
 
 class Movie extends Media {
   constructor(title, director, runTime, ratings = []) {
     super(title, ratings);
     this._director = director;
     this._runTime = runTime;
   }
 
   get director() {
     return this._director;
   }
 
   get runTime() {
     return this._runTime;
   }
 }
 
 const historyOfEverything = new Book('A Short History of Nearly Everything', 'Bill Bryson', 544);
 historyOfEverything.toggleCheckOutStatus();
 historyOfEverything.addRating(4);
 historyOfEverything.addRating(5);
 historyOfEverything.addRating(3);
 console.log(historyOfEverything.getAverageRating());
 historyOfEverything.isCheckedOut
 
 
 const speed = new Movie('Speed','Jab de Bont',116)
 
 speed.toggleCheckOutStatus()
 console.log(speed.isCheckedOut)
 speed.addRating(1);
 speed.addRating(1);
 speed.addRating(5);
 console.log(speed.getAverageRating())