import { Writable } from 'stream';
import fs from 'fs';

export class PaginatorStream extends Writable {
    constructor(targetPath, size) {
        super({ objectMode: true });
        this._targetPath = targetPath;
        this._size = size;
        this._count = 0;
        this._currentFileName = null;
        this._wstream = null;
        this._lastDepartureTime = null;
    }

    _write(data, encoding, done) {
        if (!this.currentFileName || (this.count >= this.size && data.departureTime !== this.lastDepartureTime)) {
            if (this.wstream) this.wstream.end();
            this.currentFileName = data.departureTime;
            this.wstream = fs.createWriteStream(`${this.targetPath}/${this.currentFileName}.jsonld`);
            this.wstream.write(JSON.stringify(data));
            this.count = 0;
        } else {
            this.wstream.write(',\n' + JSON.stringify(data));
        }

        this.count++;
        this.lastDepartureTime = data.departureTime;
        done();
    }

    get targetPath() {
        return this._targetPath;
    }

    get size() {
        return this._size;
    }

    get count() {
        return this._count;
    }

    set count(c) {
        this._count = c;
    }

    get currentFileName() {
        return this._currentFileName;
    }

    set currentFileName(fn) {
        this._currentFileName = fn;
    }

    get wstream() {
        return this._wstream;
    }

    set wstream(s) {
        this._wstream = s;
    }

    get lastDepartureTime() {
        return this._lastDepartureTime;
    }

    set lastDepartureTime(ldt) {
        this._lastDepartureTime = ldt;
    }
}