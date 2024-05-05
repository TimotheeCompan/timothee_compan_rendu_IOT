import bcrypt from "bcrypt";

const saltrounds = 10;

export const hashPassword = (password) => {
    return bcrypt.hash(password, saltrounds);
};

export const comparePassword = (password, hash)=>{
    return bcrypt.compare(password, hash);
}