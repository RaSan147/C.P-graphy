
function Activity(amount) {
    this.amount = amount;
}

Activity.prototype.setAmount = (value) => {
        if (value>0){
            this.amount = value;
            return true;
        }
        return false;
    }

Activity.prototype.getAmount = () => {
    return this.amount
}

    
function Payment(amount, receiver) {
    Object.setPrototypeOf(this, Activity.prototype);
	this.setAmount(amount);
    this.receiver = receiver;

}

console.log(Payment.prototype);

Payment.__proto__["setReceiver"] = (receiver) => {
    this.receiver = receiver;
}

Payment.__proto__["getReceiver"] = () => {
    return this.receiver;
}
function Refund(amount, sender) {
    this.__proto__ = Activity.prototype;
	this.setAmount(amount);
    this.sender = sender;
}
Refund.__proto__.setSender = (sender) => {
    this.sender = sender;
}

Refund.__proto__.getSender = () => {
    return this.sender;
}
let payment = new Payment(100, "John");
let refund = new Refund(50, "Jane");

payment.setAmount(200);
refund.setAmount(100);

console.log(payment.getAmount());
console.log(refund.getAmount());

console.log(Payment.prototype.hasOwnProperty("setReceiver"));
console.log(Refund.prototype.hasOwnProperty("setSender"));