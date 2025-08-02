_L='logTrapAddr'
_K='logTrapLevel'
_J='read-create'
_I='notice'
_H='warning'
_G='critical'
_F='logServerAddr'
_E='logServerLevel'
_D='read-write'
_C='FS-NMS-LOG-SERVER-MIB'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
nmslocal,=mibBuilder.importSymbols('FS-NMS-SMI','nmslocal')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
_LogServer_ObjectIdentity=ObjectIdentity
logServer=_LogServer_ObjectIdentity((1,3,6,1,4,1,52642,2,235))
_LogServerTable_Object=MibTable
logServerTable=_LogServerTable_Object((1,3,6,1,4,1,52642,2,235,1))
if mibBuilder.loadTexts:logServerTable.setStatus(_A)
_LogServerTableEntry_Object=MibTableRow
logServerTableEntry=_LogServerTableEntry_Object((1,3,6,1,4,1,52642,2,235,1,1))
logServerTableEntry.setIndexNames((0,_C,_E),(0,_C,_F))
if mibBuilder.loadTexts:logServerTableEntry.setStatus(_A)
class _LogServerLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('emerg',0),('alert',1),(_G,2),('error',3),(_H,4),(_I,5),('info',6),('debug',7)))
_LogServerLevel_Type.__name__=_B
_LogServerLevel_Object=MibTableColumn
logServerLevel=_LogServerLevel_Object((1,3,6,1,4,1,52642,2,235,1,1,1),_LogServerLevel_Type())
logServerLevel.setMaxAccess('read-only')
if mibBuilder.loadTexts:logServerLevel.setStatus(_A)
_LogServerAddr_Type=IpAddress
_LogServerAddr_Object=MibTableColumn
logServerAddr=_LogServerAddr_Object((1,3,6,1,4,1,52642,2,235,1,1,2),_LogServerAddr_Type())
logServerAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:logServerAddr.setStatus(_A)
_LogServerRowStatus_Type=RowStatus
_LogServerRowStatus_Object=MibTableColumn
logServerRowStatus=_LogServerRowStatus_Object((1,3,6,1,4,1,52642,2,235,1,1,3),_LogServerRowStatus_Type())
logServerRowStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:logServerRowStatus.setStatus(_A)
class _LogServerOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('on',0),('off',1)))
_LogServerOff_Type.__name__=_B
_LogServerOff_Object=MibScalar
logServerOff=_LogServerOff_Object((1,3,6,1,4,1,52642,2,235,2),_LogServerOff_Type())
logServerOff.setMaxAccess(_D)
if mibBuilder.loadTexts:logServerOff.setStatus(_A)
_LogTrapTable_Object=MibTable
logTrapTable=_LogTrapTable_Object((1,3,6,1,4,1,52642,2,235,3))
if mibBuilder.loadTexts:logTrapTable.setStatus(_A)
_LogTrapTableEntry_Object=MibTableRow
logTrapTableEntry=_LogTrapTableEntry_Object((1,3,6,1,4,1,52642,2,235,3,1))
logTrapTableEntry.setIndexNames((0,_C,_K),(0,_C,_L))
if mibBuilder.loadTexts:logTrapTableEntry.setStatus(_A)
_LogTrapAddr_Type=IpAddress
_LogTrapAddr_Object=MibTableColumn
logTrapAddr=_LogTrapAddr_Object((1,3,6,1,4,1,52642,2,235,3,1,1),_LogTrapAddr_Type())
logTrapAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:logTrapAddr.setStatus(_A)
_LogTrapRowStatus_Type=RowStatus
_LogTrapRowStatus_Object=MibTableColumn
logTrapRowStatus=_LogTrapRowStatus_Object((1,3,6,1,4,1,52642,2,235,3,1,2),_LogTrapRowStatus_Type())
logTrapRowStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:logTrapRowStatus.setStatus(_A)
class _LogTrapRfcVer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('RFC3164',0),('RFC5424',1)))
_LogTrapRfcVer_Type.__name__=_B
_LogTrapRfcVer_Object=MibTableColumn
logTrapRfcVer=_LogTrapRfcVer_Object((1,3,6,1,4,1,52642,2,235,3,1,3),_LogTrapRfcVer_Type())
logTrapRfcVer.setMaxAccess(_D)
if mibBuilder.loadTexts:logTrapRfcVer.setStatus(_A)
class _LogTrapLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('emerg',0),('alert',1),(_G,2),('error',3),(_H,4),(_I,5),('info',6),('debug',7)))
_LogTrapLevel_Type.__name__=_B
_LogTrapLevel_Object=MibScalar
logTrapLevel=_LogTrapLevel_Object((1,3,6,1,4,1,52642,2,235,4),_LogTrapLevel_Type())
logTrapLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:logTrapLevel.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'logServer':logServer,'logServerTable':logServerTable,'logServerTableEntry':logServerTableEntry,_E:logServerLevel,_F:logServerAddr,'logServerRowStatus':logServerRowStatus,'logServerOff':logServerOff,'logTrapTable':logTrapTable,'logTrapTableEntry':logTrapTableEntry,_L:logTrapAddr,'logTrapRowStatus':logTrapRowStatus,'logTrapRfcVer':logTrapRfcVer,_K:logTrapLevel})