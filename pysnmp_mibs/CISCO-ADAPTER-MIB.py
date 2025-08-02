_J='adptrCommunityAccess'
_I='adptrTrapReceiverAddr'
_H='adptrIndex'
_G='read-write'
_F='CISCO-ADAPTER-MIB'
_E='DisplayString'
_D='other'
_C='read-only'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
_Cisco_ObjectIdentity=ObjectIdentity
cisco=_Cisco_ObjectIdentity((1,3,6,1,4,1,9))
_Workgroup_ObjectIdentity=ObjectIdentity
workgroup=_Workgroup_ObjectIdentity((1,3,6,1,4,1,9,5))
_AdapterCard_ObjectIdentity=ObjectIdentity
adapterCard=_AdapterCard_ObjectIdentity((1,3,6,1,4,1,9,5,2))
class _AdptrNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_AdptrNumber_Type.__name__=_B
_AdptrNumber_Object=MibScalar
adptrNumber=_AdptrNumber_Object((1,3,6,1,4,1,9,5,2,1),_AdptrNumber_Type())
adptrNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:adptrNumber.setStatus(_A)
_AdptrTable_Object=MibTable
adptrTable=_AdptrTable_Object((1,3,6,1,4,1,9,5,2,2))
if mibBuilder.loadTexts:adptrTable.setStatus(_A)
_AdptrEntry_Object=MibTableRow
adptrEntry=_AdptrEntry_Object((1,3,6,1,4,1,9,5,2,2,1))
adptrEntry.setIndexNames((0,_F,_H))
if mibBuilder.loadTexts:adptrEntry.setStatus(_A)
class _AdptrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_AdptrIndex_Type.__name__=_B
_AdptrIndex_Object=MibTableColumn
adptrIndex=_AdptrIndex_Object((1,3,6,1,4,1,9,5,2,2,1,1),_AdptrIndex_Type())
adptrIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:adptrIndex.setStatus(_A)
class _AdptrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,10)));namedValues=NamedValues(*((_D,1),('sBusCddi',2),('sBusFddiSt',3),('sBusFddi',4),('mcaCddi',5),('mcaFddiSt',6),('mcaFddi',7),('eisaCddi',8),('eisaFddi',10)))
_AdptrType_Type.__name__=_B
_AdptrType_Object=MibTableColumn
adptrType=_AdptrType_Object((1,3,6,1,4,1,9,5,2,2,1,2),_AdptrType_Type())
adptrType.setMaxAccess(_C)
if mibBuilder.loadTexts:adptrType.setStatus(_A)
class _AdptrSerialNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999999999))
_AdptrSerialNumber_Type.__name__=_B
_AdptrSerialNumber_Object=MibTableColumn
adptrSerialNumber=_AdptrSerialNumber_Object((1,3,6,1,4,1,9,5,2,2,1,3),_AdptrSerialNumber_Type())
adptrSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:adptrSerialNumber.setStatus(_A)
class _AdptrHwHiVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AdptrHwHiVersion_Type.__name__=_B
_AdptrHwHiVersion_Object=MibTableColumn
adptrHwHiVersion=_AdptrHwHiVersion_Object((1,3,6,1,4,1,9,5,2,2,1,4),_AdptrHwHiVersion_Type())
adptrHwHiVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:adptrHwHiVersion.setStatus(_A)
class _AdptrHwLoVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AdptrHwLoVersion_Type.__name__=_B
_AdptrHwLoVersion_Object=MibTableColumn
adptrHwLoVersion=_AdptrHwLoVersion_Object((1,3,6,1,4,1,9,5,2,2,1,5),_AdptrHwLoVersion_Type())
adptrHwLoVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:adptrHwLoVersion.setStatus(_A)
class _AdptrFwHiVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AdptrFwHiVersion_Type.__name__=_B
_AdptrFwHiVersion_Object=MibTableColumn
adptrFwHiVersion=_AdptrFwHiVersion_Object((1,3,6,1,4,1,9,5,2,2,1,6),_AdptrFwHiVersion_Type())
adptrFwHiVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:adptrFwHiVersion.setStatus(_A)
class _AdptrFwLoVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AdptrFwLoVersion_Type.__name__=_B
_AdptrFwLoVersion_Object=MibTableColumn
adptrFwLoVersion=_AdptrFwLoVersion_Object((1,3,6,1,4,1,9,5,2,2,1,7),_AdptrFwLoVersion_Type())
adptrFwLoVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:adptrFwLoVersion.setStatus(_A)
class _AdptrSwHiVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AdptrSwHiVersion_Type.__name__=_B
_AdptrSwHiVersion_Object=MibTableColumn
adptrSwHiVersion=_AdptrSwHiVersion_Object((1,3,6,1,4,1,9,5,2,2,1,8),_AdptrSwHiVersion_Type())
adptrSwHiVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:adptrSwHiVersion.setStatus(_A)
class _AdptrSwLoVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AdptrSwLoVersion_Type.__name__=_B
_AdptrSwLoVersion_Object=MibTableColumn
adptrSwLoVersion=_AdptrSwLoVersion_Object((1,3,6,1,4,1,9,5,2,2,1,9),_AdptrSwLoVersion_Type())
adptrSwLoVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:adptrSwLoVersion.setStatus(_A)
class _AdptrStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_D,1),('ok',2),('minorFault',3),('majorFault',4)))
_AdptrStatus_Type.__name__=_B
_AdptrStatus_Object=MibTableColumn
adptrStatus=_AdptrStatus_Object((1,3,6,1,4,1,9,5,2,2,1,10),_AdptrStatus_Type())
adptrStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:adptrStatus.setStatus(_A)
class _AdptrSelfTestResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AdptrSelfTestResult_Type.__name__=_B
_AdptrSelfTestResult_Object=MibTableColumn
adptrSelfTestResult=_AdptrSelfTestResult_Object((1,3,6,1,4,1,9,5,2,2,1,11),_AdptrSelfTestResult_Type())
adptrSelfTestResult.setMaxAccess(_C)
if mibBuilder.loadTexts:adptrSelfTestResult.setStatus(_A)
class _AdptrDriverHiVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AdptrDriverHiVersion_Type.__name__=_B
_AdptrDriverHiVersion_Object=MibTableColumn
adptrDriverHiVersion=_AdptrDriverHiVersion_Object((1,3,6,1,4,1,9,5,2,2,1,13),_AdptrDriverHiVersion_Type())
adptrDriverHiVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:adptrDriverHiVersion.setStatus(_A)
class _AdptrDriverLoVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AdptrDriverLoVersion_Type.__name__=_B
_AdptrDriverLoVersion_Object=MibTableColumn
adptrDriverLoVersion=_AdptrDriverLoVersion_Object((1,3,6,1,4,1,9,5,2,2,1,14),_AdptrDriverLoVersion_Type())
adptrDriverLoVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:adptrDriverLoVersion.setStatus(_A)
class _AdptrMediaType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_D,1),('cddi',2),('fiber',3),('tppmd',4),('mlt3',5),('sddi',6),('smf',7)))
_AdptrMediaType_Type.__name__=_B
_AdptrMediaType_Object=MibTableColumn
adptrMediaType=_AdptrMediaType_Object((1,3,6,1,4,1,9,5,2,2,1,17),_AdptrMediaType_Type())
adptrMediaType.setMaxAccess(_C)
if mibBuilder.loadTexts:adptrMediaType.setStatus(_A)
class _AdptrModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_AdptrModel_Type.__name__=_E
_AdptrModel_Object=MibTableColumn
adptrModel=_AdptrModel_Object((1,3,6,1,4,1,9,5,2,2,1,18),_AdptrModel_Type())
adptrModel.setMaxAccess(_C)
if mibBuilder.loadTexts:adptrModel.setStatus(_A)
_AdptrTrapReceiverTable_Object=MibTable
adptrTrapReceiverTable=_AdptrTrapReceiverTable_Object((1,3,6,1,4,1,9,5,2,3))
if mibBuilder.loadTexts:adptrTrapReceiverTable.setStatus(_A)
_AdptrTrapReceiverEntry_Object=MibTableRow
adptrTrapReceiverEntry=_AdptrTrapReceiverEntry_Object((1,3,6,1,4,1,9,5,2,3,1))
adptrTrapReceiverEntry.setIndexNames((0,_F,_I))
if mibBuilder.loadTexts:adptrTrapReceiverEntry.setStatus(_A)
class _AdptrTrapReceiverType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),('invalid',2)))
_AdptrTrapReceiverType_Type.__name__=_B
_AdptrTrapReceiverType_Object=MibTableColumn
adptrTrapReceiverType=_AdptrTrapReceiverType_Object((1,3,6,1,4,1,9,5,2,3,1,1),_AdptrTrapReceiverType_Type())
adptrTrapReceiverType.setMaxAccess(_G)
if mibBuilder.loadTexts:adptrTrapReceiverType.setStatus(_A)
_AdptrTrapReceiverAddr_Type=IpAddress
_AdptrTrapReceiverAddr_Object=MibTableColumn
adptrTrapReceiverAddr=_AdptrTrapReceiverAddr_Object((1,3,6,1,4,1,9,5,2,3,1,2),_AdptrTrapReceiverAddr_Type())
adptrTrapReceiverAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:adptrTrapReceiverAddr.setStatus(_A)
class _AdptrTrapReceiverComm_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_AdptrTrapReceiverComm_Type.__name__=_E
_AdptrTrapReceiverComm_Object=MibTableColumn
adptrTrapReceiverComm=_AdptrTrapReceiverComm_Object((1,3,6,1,4,1,9,5,2,3,1,3),_AdptrTrapReceiverComm_Type())
adptrTrapReceiverComm.setMaxAccess(_G)
if mibBuilder.loadTexts:adptrTrapReceiverComm.setStatus(_A)
_AdptrCommunityTable_Object=MibTable
adptrCommunityTable=_AdptrCommunityTable_Object((1,3,6,1,4,1,9,5,2,4))
if mibBuilder.loadTexts:adptrCommunityTable.setStatus(_A)
_AdptrCommunityEntry_Object=MibTableRow
adptrCommunityEntry=_AdptrCommunityEntry_Object((1,3,6,1,4,1,9,5,2,4,1))
adptrCommunityEntry.setIndexNames((0,_F,_J))
if mibBuilder.loadTexts:adptrCommunityEntry.setStatus(_A)
class _AdptrCommunityAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_D,1),('readOnly',2),('readWrite',3),('readWriteAll',4)))
_AdptrCommunityAccess_Type.__name__=_B
_AdptrCommunityAccess_Object=MibTableColumn
adptrCommunityAccess=_AdptrCommunityAccess_Object((1,3,6,1,4,1,9,5,2,4,1,1),_AdptrCommunityAccess_Type())
adptrCommunityAccess.setMaxAccess(_C)
if mibBuilder.loadTexts:adptrCommunityAccess.setStatus(_A)
class _AdptrCommunityString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_AdptrCommunityString_Type.__name__=_E
_AdptrCommunityString_Object=MibTableColumn
adptrCommunityString=_AdptrCommunityString_Object((1,3,6,1,4,1,9,5,2,4,1,2),_AdptrCommunityString_Type())
adptrCommunityString.setMaxAccess(_G)
if mibBuilder.loadTexts:adptrCommunityString.setStatus(_A)
class _AdptrMgmtType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('snmp',2),('smux',3)))
_AdptrMgmtType_Type.__name__=_B
_AdptrMgmtType_Object=MibScalar
adptrMgmtType=_AdptrMgmtType_Object((1,3,6,1,4,1,9,5,2,5),_AdptrMgmtType_Type())
adptrMgmtType.setMaxAccess(_C)
if mibBuilder.loadTexts:adptrMgmtType.setStatus(_A)
class _AdptrMgmtHiVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AdptrMgmtHiVersion_Type.__name__=_B
_AdptrMgmtHiVersion_Object=MibScalar
adptrMgmtHiVersion=_AdptrMgmtHiVersion_Object((1,3,6,1,4,1,9,5,2,6),_AdptrMgmtHiVersion_Type())
adptrMgmtHiVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:adptrMgmtHiVersion.setStatus(_A)
class _AdptrMgmtLoVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AdptrMgmtLoVersion_Type.__name__=_B
_AdptrMgmtLoVersion_Object=MibScalar
adptrMgmtLoVersion=_AdptrMgmtLoVersion_Object((1,3,6,1,4,1,9,5,2,7),_AdptrMgmtLoVersion_Type())
adptrMgmtLoVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:adptrMgmtLoVersion.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'cisco':cisco,'workgroup':workgroup,'adapterCard':adapterCard,'adptrNumber':adptrNumber,'adptrTable':adptrTable,'adptrEntry':adptrEntry,_H:adptrIndex,'adptrType':adptrType,'adptrSerialNumber':adptrSerialNumber,'adptrHwHiVersion':adptrHwHiVersion,'adptrHwLoVersion':adptrHwLoVersion,'adptrFwHiVersion':adptrFwHiVersion,'adptrFwLoVersion':adptrFwLoVersion,'adptrSwHiVersion':adptrSwHiVersion,'adptrSwLoVersion':adptrSwLoVersion,'adptrStatus':adptrStatus,'adptrSelfTestResult':adptrSelfTestResult,'adptrDriverHiVersion':adptrDriverHiVersion,'adptrDriverLoVersion':adptrDriverLoVersion,'adptrMediaType':adptrMediaType,'adptrModel':adptrModel,'adptrTrapReceiverTable':adptrTrapReceiverTable,'adptrTrapReceiverEntry':adptrTrapReceiverEntry,'adptrTrapReceiverType':adptrTrapReceiverType,_I:adptrTrapReceiverAddr,'adptrTrapReceiverComm':adptrTrapReceiverComm,'adptrCommunityTable':adptrCommunityTable,'adptrCommunityEntry':adptrCommunityEntry,_J:adptrCommunityAccess,'adptrCommunityString':adptrCommunityString,'adptrMgmtType':adptrMgmtType,'adptrMgmtHiVersion':adptrMgmtHiVersion,'adptrMgmtLoVersion':adptrMgmtLoVersion})