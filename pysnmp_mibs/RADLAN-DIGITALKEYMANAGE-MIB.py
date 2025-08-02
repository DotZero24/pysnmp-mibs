_I='rlMD5KeyChainKeyId'
_H='rlMD5KeyChainName'
_G='DisplayString'
_F='Integer32'
_E='RADLAN-DIGITALKEYMANAGE-MIB'
_D='TruthValue'
_C='read-only'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rnd,=mibBuilder.importSymbols('RADLAN-MIB','rnd')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_G,'PhysAddress','RowStatus','TextualConvention',_D)
rlDigitalKeyManage=ModuleIdentity((1,3,6,1,4,1,89,86))
if mibBuilder.loadTexts:rlDigitalKeyManage.setRevisions(('2007-01-02 00:00',))
_RlMD5KeyChainTable_Object=MibTable
rlMD5KeyChainTable=_RlMD5KeyChainTable_Object((1,3,6,1,4,1,89,86,1))
if mibBuilder.loadTexts:rlMD5KeyChainTable.setStatus(_A)
_RlMD5KeyChainEntry_Object=MibTableRow
rlMD5KeyChainEntry=_RlMD5KeyChainEntry_Object((1,3,6,1,4,1,89,86,1,1))
rlMD5KeyChainEntry.setIndexNames((0,_E,_H),(0,_E,_I))
if mibBuilder.loadTexts:rlMD5KeyChainEntry.setStatus(_A)
_RlMD5KeyChainName_Type=DisplayString
_RlMD5KeyChainName_Object=MibTableColumn
rlMD5KeyChainName=_RlMD5KeyChainName_Object((1,3,6,1,4,1,89,86,1,1,1),_RlMD5KeyChainName_Type())
rlMD5KeyChainName.setMaxAccess(_C)
if mibBuilder.loadTexts:rlMD5KeyChainName.setStatus(_A)
class _RlMD5KeyChainKeyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_RlMD5KeyChainKeyId_Type.__name__=_F
_RlMD5KeyChainKeyId_Object=MibTableColumn
rlMD5KeyChainKeyId=_RlMD5KeyChainKeyId_Object((1,3,6,1,4,1,89,86,1,1,2),_RlMD5KeyChainKeyId_Type())
rlMD5KeyChainKeyId.setMaxAccess(_C)
if mibBuilder.loadTexts:rlMD5KeyChainKeyId.setStatus(_A)
class _RlMD5KeyChainKey_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_RlMD5KeyChainKey_Type.__name__=_G
_RlMD5KeyChainKey_Object=MibTableColumn
rlMD5KeyChainKey=_RlMD5KeyChainKey_Object((1,3,6,1,4,1,89,86,1,1,3),_RlMD5KeyChainKey_Type())
rlMD5KeyChainKey.setMaxAccess(_B)
if mibBuilder.loadTexts:rlMD5KeyChainKey.setStatus(_A)
_RlMD5KeyChainKeyStartAccept_Type=DateAndTime
_RlMD5KeyChainKeyStartAccept_Object=MibTableColumn
rlMD5KeyChainKeyStartAccept=_RlMD5KeyChainKeyStartAccept_Object((1,3,6,1,4,1,89,86,1,1,4),_RlMD5KeyChainKeyStartAccept_Type())
rlMD5KeyChainKeyStartAccept.setMaxAccess(_B)
if mibBuilder.loadTexts:rlMD5KeyChainKeyStartAccept.setStatus(_A)
_RlMD5KeyChainKeyStartGenerate_Type=DateAndTime
_RlMD5KeyChainKeyStartGenerate_Object=MibTableColumn
rlMD5KeyChainKeyStartGenerate=_RlMD5KeyChainKeyStartGenerate_Object((1,3,6,1,4,1,89,86,1,1,5),_RlMD5KeyChainKeyStartGenerate_Type())
rlMD5KeyChainKeyStartGenerate.setMaxAccess(_B)
if mibBuilder.loadTexts:rlMD5KeyChainKeyStartGenerate.setStatus(_A)
_RlMD5KeyChainKeyStopGenerate_Type=DateAndTime
_RlMD5KeyChainKeyStopGenerate_Object=MibTableColumn
rlMD5KeyChainKeyStopGenerate=_RlMD5KeyChainKeyStopGenerate_Object((1,3,6,1,4,1,89,86,1,1,6),_RlMD5KeyChainKeyStopGenerate_Type())
rlMD5KeyChainKeyStopGenerate.setMaxAccess(_B)
if mibBuilder.loadTexts:rlMD5KeyChainKeyStopGenerate.setStatus(_A)
_RlMD5KeyChainKeyStopAccept_Type=DateAndTime
_RlMD5KeyChainKeyStopAccept_Object=MibTableColumn
rlMD5KeyChainKeyStopAccept=_RlMD5KeyChainKeyStopAccept_Object((1,3,6,1,4,1,89,86,1,1,7),_RlMD5KeyChainKeyStopAccept_Type())
rlMD5KeyChainKeyStopAccept.setMaxAccess(_B)
if mibBuilder.loadTexts:rlMD5KeyChainKeyStopAccept.setStatus(_A)
class _RlMD5KeyChainKeyValidForAccept_Type(TruthValue):defaultValue=2
_RlMD5KeyChainKeyValidForAccept_Type.__name__=_D
_RlMD5KeyChainKeyValidForAccept_Object=MibTableColumn
rlMD5KeyChainKeyValidForAccept=_RlMD5KeyChainKeyValidForAccept_Object((1,3,6,1,4,1,89,86,1,1,8),_RlMD5KeyChainKeyValidForAccept_Type())
rlMD5KeyChainKeyValidForAccept.setMaxAccess(_C)
if mibBuilder.loadTexts:rlMD5KeyChainKeyValidForAccept.setStatus(_A)
class _RlMD5KeyChainKeyValidForGenerate_Type(TruthValue):defaultValue=2
_RlMD5KeyChainKeyValidForGenerate_Type.__name__=_D
_RlMD5KeyChainKeyValidForGenerate_Object=MibTableColumn
rlMD5KeyChainKeyValidForGenerate=_RlMD5KeyChainKeyValidForGenerate_Object((1,3,6,1,4,1,89,86,1,1,9),_RlMD5KeyChainKeyValidForGenerate_Type())
rlMD5KeyChainKeyValidForGenerate.setMaxAccess(_C)
if mibBuilder.loadTexts:rlMD5KeyChainKeyValidForGenerate.setStatus(_A)
_RlMD5KeyChainRowStatus_Type=RowStatus
_RlMD5KeyChainRowStatus_Object=MibTableColumn
rlMD5KeyChainRowStatus=_RlMD5KeyChainRowStatus_Object((1,3,6,1,4,1,89,86,1,1,10),_RlMD5KeyChainRowStatus_Type())
rlMD5KeyChainRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlMD5KeyChainRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'rlDigitalKeyManage':rlDigitalKeyManage,'rlMD5KeyChainTable':rlMD5KeyChainTable,'rlMD5KeyChainEntry':rlMD5KeyChainEntry,_H:rlMD5KeyChainName,_I:rlMD5KeyChainKeyId,'rlMD5KeyChainKey':rlMD5KeyChainKey,'rlMD5KeyChainKeyStartAccept':rlMD5KeyChainKeyStartAccept,'rlMD5KeyChainKeyStartGenerate':rlMD5KeyChainKeyStartGenerate,'rlMD5KeyChainKeyStopGenerate':rlMD5KeyChainKeyStopGenerate,'rlMD5KeyChainKeyStopAccept':rlMD5KeyChainKeyStopAccept,'rlMD5KeyChainKeyValidForAccept':rlMD5KeyChainKeyValidForAccept,'rlMD5KeyChainKeyValidForGenerate':rlMD5KeyChainKeyValidForGenerate,'rlMD5KeyChainRowStatus':rlMD5KeyChainRowStatus})