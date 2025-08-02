_W='bsoeVirtIfMessageDigestType'
_V='bsoeVirtIfMessageDigestIndex'
_U='bsoeVirtIfMessageDigestNeighbor'
_T='bsoeVirtIfMessageDigestAreaId'
_S='bsoeOspfVirtIfExtNeighbor'
_R='bsoeOspfVirtIfExtAreaId'
_Q='bsoeOspfNbrExtAddressLessIndex'
_P='bsoeOspfNbrExtIpAddr'
_O='bsoeMessageDigestType'
_N='bsoeMessageDigestIndex'
_M='bsoeMessageDigestAddressLessIf'
_L='bsoeMessageDigestIpAddress'
_K='bsoeOspfAddressLessIf'
_J='bsoeOspfIfIpAddress'
_I='read-only'
_H='TruthValue'
_G='OctetString'
_F='read-create'
_E='read-write'
_D='not-accessible'
_C='Integer32'
_B='BAY-STACK-OSPF-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
AreaID,RouterID=mibBuilder.importSymbols('OSPF-MIB','AreaID','RouterID')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_H)
bayStackMibs,=mibBuilder.importSymbols('SYNOPTICS-ROOT-MIB','bayStackMibs')
bayStackOspfExtMib=ModuleIdentity((1,3,6,1,4,1,45,5,14))
if mibBuilder.loadTexts:bayStackOspfExtMib.setRevisions(('2010-07-13 00:00','2009-11-10 00:00','2006-09-26 00:00','2006-09-14 00:00','2006-06-13 00:00','2005-12-01 00:00','2005-10-20 00:00','2005-10-11 00:00','2005-09-08 00:00'))
_BsoeNotifications_ObjectIdentity=ObjectIdentity
bsoeNotifications=_BsoeNotifications_ObjectIdentity((1,3,6,1,4,1,45,5,14,0))
_BsoeObjects_ObjectIdentity=ObjectIdentity
bsoeObjects=_BsoeObjects_ObjectIdentity((1,3,6,1,4,1,45,5,14,1))
_BsoeScalars_ObjectIdentity=ObjectIdentity
bsoeScalars=_BsoeScalars_ObjectIdentity((1,3,6,1,4,1,45,5,14,1,1))
class _BsoeApplyRedistribute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('none',0),('direct',1),('static',2),('rip',3),('ospf',4),('bgp',5)))
_BsoeApplyRedistribute_Type.__name__=_C
_BsoeApplyRedistribute_Object=MibScalar
bsoeApplyRedistribute=_BsoeApplyRedistribute_Object((1,3,6,1,4,1,45,5,14,1,1,1),_BsoeApplyRedistribute_Type())
bsoeApplyRedistribute.setMaxAccess(_E)
if mibBuilder.loadTexts:bsoeApplyRedistribute.setStatus(_A)
class _BsoeHardwareCompatibilityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ers5510',1),('noneErs5510',2)))
_BsoeHardwareCompatibilityMode_Type.__name__=_C
_BsoeHardwareCompatibilityMode_Object=MibScalar
bsoeHardwareCompatibilityMode=_BsoeHardwareCompatibilityMode_Object((1,3,6,1,4,1,45,5,14,1,1,2),_BsoeHardwareCompatibilityMode_Type())
bsoeHardwareCompatibilityMode.setMaxAccess(_E)
if mibBuilder.loadTexts:bsoeHardwareCompatibilityMode.setStatus(_A)
_BsoeOspfIfExtTable_Object=MibTable
bsoeOspfIfExtTable=_BsoeOspfIfExtTable_Object((1,3,6,1,4,1,45,5,14,1,2))
if mibBuilder.loadTexts:bsoeOspfIfExtTable.setStatus(_A)
_BsoeOspfIfExtEntry_Object=MibTableRow
bsoeOspfIfExtEntry=_BsoeOspfIfExtEntry_Object((1,3,6,1,4,1,45,5,14,1,2,1))
bsoeOspfIfExtEntry.setIndexNames((0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:bsoeOspfIfExtEntry.setStatus(_A)
_BsoeOspfIfIpAddress_Type=IpAddress
_BsoeOspfIfIpAddress_Object=MibTableColumn
bsoeOspfIfIpAddress=_BsoeOspfIfIpAddress_Object((1,3,6,1,4,1,45,5,14,1,2,1,1),_BsoeOspfIfIpAddress_Type())
bsoeOspfIfIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:bsoeOspfIfIpAddress.setStatus(_A)
class _BsoeOspfAddressLessIf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_BsoeOspfAddressLessIf_Type.__name__=_C
_BsoeOspfAddressLessIf_Object=MibTableColumn
bsoeOspfAddressLessIf=_BsoeOspfAddressLessIf_Object((1,3,6,1,4,1,45,5,14,1,2,1,2),_BsoeOspfAddressLessIf_Type())
bsoeOspfAddressLessIf.setMaxAccess(_D)
if mibBuilder.loadTexts:bsoeOspfAddressLessIf.setStatus(_A)
class _BsoeOspfIfExtAdvertiseWhenDown_Type(TruthValue):defaultValue=2
_BsoeOspfIfExtAdvertiseWhenDown_Type.__name__=_H
_BsoeOspfIfExtAdvertiseWhenDown_Object=MibTableColumn
bsoeOspfIfExtAdvertiseWhenDown=_BsoeOspfIfExtAdvertiseWhenDown_Object((1,3,6,1,4,1,45,5,14,1,2,1,3),_BsoeOspfIfExtAdvertiseWhenDown_Type())
bsoeOspfIfExtAdvertiseWhenDown.setMaxAccess(_E)
if mibBuilder.loadTexts:bsoeOspfIfExtAdvertiseWhenDown.setStatus(_A)
class _BsoeOspfIfExtPrimaryMd5Key_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BsoeOspfIfExtPrimaryMd5Key_Type.__name__=_C
_BsoeOspfIfExtPrimaryMd5Key_Object=MibTableColumn
bsoeOspfIfExtPrimaryMd5Key=_BsoeOspfIfExtPrimaryMd5Key_Object((1,3,6,1,4,1,45,5,14,1,2,1,4),_BsoeOspfIfExtPrimaryMd5Key_Type())
bsoeOspfIfExtPrimaryMd5Key.setMaxAccess(_E)
if mibBuilder.loadTexts:bsoeOspfIfExtPrimaryMd5Key.setStatus(_A)
class _BsoeOspfIfExtMtuIgnore_Type(TruthValue):defaultValue=2
_BsoeOspfIfExtMtuIgnore_Type.__name__=_H
_BsoeOspfIfExtMtuIgnore_Object=MibTableColumn
bsoeOspfIfExtMtuIgnore=_BsoeOspfIfExtMtuIgnore_Object((1,3,6,1,4,1,45,5,14,1,2,1,5),_BsoeOspfIfExtMtuIgnore_Type())
bsoeOspfIfExtMtuIgnore.setMaxAccess(_E)
if mibBuilder.loadTexts:bsoeOspfIfExtMtuIgnore.setStatus(_A)
class _BsoeOspfIfExtType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('other',1),('passive',2)))
_BsoeOspfIfExtType_Type.__name__=_C
_BsoeOspfIfExtType_Object=MibTableColumn
bsoeOspfIfExtType=_BsoeOspfIfExtType_Object((1,3,6,1,4,1,45,5,14,1,2,1,6),_BsoeOspfIfExtType_Type())
bsoeOspfIfExtType.setMaxAccess(_E)
if mibBuilder.loadTexts:bsoeOspfIfExtType.setStatus(_A)
_BsoeMessageDigestTable_Object=MibTable
bsoeMessageDigestTable=_BsoeMessageDigestTable_Object((1,3,6,1,4,1,45,5,14,1,3))
if mibBuilder.loadTexts:bsoeMessageDigestTable.setStatus(_A)
_BsoeMessageDigestEntry_Object=MibTableRow
bsoeMessageDigestEntry=_BsoeMessageDigestEntry_Object((1,3,6,1,4,1,45,5,14,1,3,1))
bsoeMessageDigestEntry.setIndexNames((0,_B,_L),(0,_B,_M),(0,_B,_N),(0,_B,_O))
if mibBuilder.loadTexts:bsoeMessageDigestEntry.setStatus(_A)
_BsoeMessageDigestIpAddress_Type=IpAddress
_BsoeMessageDigestIpAddress_Object=MibTableColumn
bsoeMessageDigestIpAddress=_BsoeMessageDigestIpAddress_Object((1,3,6,1,4,1,45,5,14,1,3,1,1),_BsoeMessageDigestIpAddress_Type())
bsoeMessageDigestIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:bsoeMessageDigestIpAddress.setStatus(_A)
class _BsoeMessageDigestAddressLessIf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_BsoeMessageDigestAddressLessIf_Type.__name__=_C
_BsoeMessageDigestAddressLessIf_Object=MibTableColumn
bsoeMessageDigestAddressLessIf=_BsoeMessageDigestAddressLessIf_Object((1,3,6,1,4,1,45,5,14,1,3,1,2),_BsoeMessageDigestAddressLessIf_Type())
bsoeMessageDigestAddressLessIf.setMaxAccess(_D)
if mibBuilder.loadTexts:bsoeMessageDigestAddressLessIf.setStatus(_A)
class _BsoeMessageDigestIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_BsoeMessageDigestIndex_Type.__name__=_C
_BsoeMessageDigestIndex_Object=MibTableColumn
bsoeMessageDigestIndex=_BsoeMessageDigestIndex_Object((1,3,6,1,4,1,45,5,14,1,3,1,3),_BsoeMessageDigestIndex_Type())
bsoeMessageDigestIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:bsoeMessageDigestIndex.setStatus(_A)
class _BsoeMessageDigestType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('md5',1))
_BsoeMessageDigestType_Type.__name__=_C
_BsoeMessageDigestType_Object=MibTableColumn
bsoeMessageDigestType=_BsoeMessageDigestType_Object((1,3,6,1,4,1,45,5,14,1,3,1,4),_BsoeMessageDigestType_Type())
bsoeMessageDigestType.setMaxAccess(_D)
if mibBuilder.loadTexts:bsoeMessageDigestType.setStatus(_A)
class _BsoeMessageDigestKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_BsoeMessageDigestKey_Type.__name__=_G
_BsoeMessageDigestKey_Object=MibTableColumn
bsoeMessageDigestKey=_BsoeMessageDigestKey_Object((1,3,6,1,4,1,45,5,14,1,3,1,5),_BsoeMessageDigestKey_Type())
bsoeMessageDigestKey.setMaxAccess(_F)
if mibBuilder.loadTexts:bsoeMessageDigestKey.setStatus(_A)
_BsoeMessageDigestRowStatus_Type=RowStatus
_BsoeMessageDigestRowStatus_Object=MibTableColumn
bsoeMessageDigestRowStatus=_BsoeMessageDigestRowStatus_Object((1,3,6,1,4,1,45,5,14,1,3,1,6),_BsoeMessageDigestRowStatus_Type())
bsoeMessageDigestRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:bsoeMessageDigestRowStatus.setStatus(_A)
_BsoeOspfNbrExtTable_Object=MibTable
bsoeOspfNbrExtTable=_BsoeOspfNbrExtTable_Object((1,3,6,1,4,1,45,5,14,1,4))
if mibBuilder.loadTexts:bsoeOspfNbrExtTable.setStatus(_A)
_BsoeOspfNbrExtEntry_Object=MibTableRow
bsoeOspfNbrExtEntry=_BsoeOspfNbrExtEntry_Object((1,3,6,1,4,1,45,5,14,1,4,1))
bsoeOspfNbrExtEntry.setIndexNames((0,_B,_P),(0,_B,_Q))
if mibBuilder.loadTexts:bsoeOspfNbrExtEntry.setStatus(_A)
_BsoeOspfNbrExtIpAddr_Type=IpAddress
_BsoeOspfNbrExtIpAddr_Object=MibTableColumn
bsoeOspfNbrExtIpAddr=_BsoeOspfNbrExtIpAddr_Object((1,3,6,1,4,1,45,5,14,1,4,1,1),_BsoeOspfNbrExtIpAddr_Type())
bsoeOspfNbrExtIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:bsoeOspfNbrExtIpAddr.setStatus(_A)
_BsoeOspfNbrExtAddressLessIndex_Type=InterfaceIndex
_BsoeOspfNbrExtAddressLessIndex_Object=MibTableColumn
bsoeOspfNbrExtAddressLessIndex=_BsoeOspfNbrExtAddressLessIndex_Object((1,3,6,1,4,1,45,5,14,1,4,1,2),_BsoeOspfNbrExtAddressLessIndex_Type())
bsoeOspfNbrExtAddressLessIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:bsoeOspfNbrExtAddressLessIndex.setStatus(_A)
_BsoeOspfNbrExtInterfaceAddr_Type=IpAddress
_BsoeOspfNbrExtInterfaceAddr_Object=MibTableColumn
bsoeOspfNbrExtInterfaceAddr=_BsoeOspfNbrExtInterfaceAddr_Object((1,3,6,1,4,1,45,5,14,1,4,1,3),_BsoeOspfNbrExtInterfaceAddr_Type())
bsoeOspfNbrExtInterfaceAddr.setMaxAccess(_I)
if mibBuilder.loadTexts:bsoeOspfNbrExtInterfaceAddr.setStatus(_A)
class _BsoeOspfNbrExtAdjacencyErrorCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*(('noError',1),('unknownError',2),('configOptE',3),('configOptN',4),('helloIntMismatch',5),('deadIntMismatch',6),('netMaskMismatch',7),('ospfVer',8),('areaMismatch',9),('authMismatch',10),('authFail',11),('noneDRBDR',12),('localRidNotSeen',13),('seqNr',14),('lsReq',15),('noFreeAdjAvail',16)))
_BsoeOspfNbrExtAdjacencyErrorCode_Type.__name__=_C
_BsoeOspfNbrExtAdjacencyErrorCode_Object=MibTableColumn
bsoeOspfNbrExtAdjacencyErrorCode=_BsoeOspfNbrExtAdjacencyErrorCode_Object((1,3,6,1,4,1,45,5,14,1,4,1,4),_BsoeOspfNbrExtAdjacencyErrorCode_Type())
bsoeOspfNbrExtAdjacencyErrorCode.setMaxAccess(_I)
if mibBuilder.loadTexts:bsoeOspfNbrExtAdjacencyErrorCode.setStatus(_A)
_BsoeOspfVirtIfExtTable_Object=MibTable
bsoeOspfVirtIfExtTable=_BsoeOspfVirtIfExtTable_Object((1,3,6,1,4,1,45,5,14,1,5))
if mibBuilder.loadTexts:bsoeOspfVirtIfExtTable.setStatus(_A)
_BsoeOspfVirtIfExtEntry_Object=MibTableRow
bsoeOspfVirtIfExtEntry=_BsoeOspfVirtIfExtEntry_Object((1,3,6,1,4,1,45,5,14,1,5,1))
bsoeOspfVirtIfExtEntry.setIndexNames((0,_B,_R),(0,_B,_S))
if mibBuilder.loadTexts:bsoeOspfVirtIfExtEntry.setStatus(_A)
_BsoeOspfVirtIfExtAreaId_Type=AreaID
_BsoeOspfVirtIfExtAreaId_Object=MibTableColumn
bsoeOspfVirtIfExtAreaId=_BsoeOspfVirtIfExtAreaId_Object((1,3,6,1,4,1,45,5,14,1,5,1,1),_BsoeOspfVirtIfExtAreaId_Type())
bsoeOspfVirtIfExtAreaId.setMaxAccess(_D)
if mibBuilder.loadTexts:bsoeOspfVirtIfExtAreaId.setStatus(_A)
_BsoeOspfVirtIfExtNeighbor_Type=RouterID
_BsoeOspfVirtIfExtNeighbor_Object=MibTableColumn
bsoeOspfVirtIfExtNeighbor=_BsoeOspfVirtIfExtNeighbor_Object((1,3,6,1,4,1,45,5,14,1,5,1,2),_BsoeOspfVirtIfExtNeighbor_Type())
bsoeOspfVirtIfExtNeighbor.setMaxAccess(_D)
if mibBuilder.loadTexts:bsoeOspfVirtIfExtNeighbor.setStatus(_A)
class _BsoeOspfVirtIfExtPrimaryMd5Key_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BsoeOspfVirtIfExtPrimaryMd5Key_Type.__name__=_C
_BsoeOspfVirtIfExtPrimaryMd5Key_Object=MibTableColumn
bsoeOspfVirtIfExtPrimaryMd5Key=_BsoeOspfVirtIfExtPrimaryMd5Key_Object((1,3,6,1,4,1,45,5,14,1,5,1,3),_BsoeOspfVirtIfExtPrimaryMd5Key_Type())
bsoeOspfVirtIfExtPrimaryMd5Key.setMaxAccess(_E)
if mibBuilder.loadTexts:bsoeOspfVirtIfExtPrimaryMd5Key.setStatus(_A)
class _BsoeOspfVirtIfExtType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('manual',1),('automatic',2)))
_BsoeOspfVirtIfExtType_Type.__name__=_C
_BsoeOspfVirtIfExtType_Object=MibTableColumn
bsoeOspfVirtIfExtType=_BsoeOspfVirtIfExtType_Object((1,3,6,1,4,1,45,5,14,1,5,1,4),_BsoeOspfVirtIfExtType_Type())
bsoeOspfVirtIfExtType.setMaxAccess(_I)
if mibBuilder.loadTexts:bsoeOspfVirtIfExtType.setStatus(_A)
_BsoeVirtIfMessageDigestTable_Object=MibTable
bsoeVirtIfMessageDigestTable=_BsoeVirtIfMessageDigestTable_Object((1,3,6,1,4,1,45,5,14,1,6))
if mibBuilder.loadTexts:bsoeVirtIfMessageDigestTable.setStatus(_A)
_BsoeVirtIfMessageDigestEntry_Object=MibTableRow
bsoeVirtIfMessageDigestEntry=_BsoeVirtIfMessageDigestEntry_Object((1,3,6,1,4,1,45,5,14,1,6,1))
bsoeVirtIfMessageDigestEntry.setIndexNames((0,_B,_T),(0,_B,_U),(0,_B,_V),(0,_B,_W))
if mibBuilder.loadTexts:bsoeVirtIfMessageDigestEntry.setStatus(_A)
_BsoeVirtIfMessageDigestAreaId_Type=AreaID
_BsoeVirtIfMessageDigestAreaId_Object=MibTableColumn
bsoeVirtIfMessageDigestAreaId=_BsoeVirtIfMessageDigestAreaId_Object((1,3,6,1,4,1,45,5,14,1,6,1,1),_BsoeVirtIfMessageDigestAreaId_Type())
bsoeVirtIfMessageDigestAreaId.setMaxAccess(_D)
if mibBuilder.loadTexts:bsoeVirtIfMessageDigestAreaId.setStatus(_A)
_BsoeVirtIfMessageDigestNeighbor_Type=RouterID
_BsoeVirtIfMessageDigestNeighbor_Object=MibTableColumn
bsoeVirtIfMessageDigestNeighbor=_BsoeVirtIfMessageDigestNeighbor_Object((1,3,6,1,4,1,45,5,14,1,6,1,2),_BsoeVirtIfMessageDigestNeighbor_Type())
bsoeVirtIfMessageDigestNeighbor.setMaxAccess(_D)
if mibBuilder.loadTexts:bsoeVirtIfMessageDigestNeighbor.setStatus(_A)
class _BsoeVirtIfMessageDigestIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_BsoeVirtIfMessageDigestIndex_Type.__name__=_C
_BsoeVirtIfMessageDigestIndex_Object=MibTableColumn
bsoeVirtIfMessageDigestIndex=_BsoeVirtIfMessageDigestIndex_Object((1,3,6,1,4,1,45,5,14,1,6,1,3),_BsoeVirtIfMessageDigestIndex_Type())
bsoeVirtIfMessageDigestIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:bsoeVirtIfMessageDigestIndex.setStatus(_A)
class _BsoeVirtIfMessageDigestType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('md5',1))
_BsoeVirtIfMessageDigestType_Type.__name__=_C
_BsoeVirtIfMessageDigestType_Object=MibTableColumn
bsoeVirtIfMessageDigestType=_BsoeVirtIfMessageDigestType_Object((1,3,6,1,4,1,45,5,14,1,6,1,4),_BsoeVirtIfMessageDigestType_Type())
bsoeVirtIfMessageDigestType.setMaxAccess(_D)
if mibBuilder.loadTexts:bsoeVirtIfMessageDigestType.setStatus(_A)
class _BsoeVirtIfMessageDigestKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_BsoeVirtIfMessageDigestKey_Type.__name__=_G
_BsoeVirtIfMessageDigestKey_Object=MibTableColumn
bsoeVirtIfMessageDigestKey=_BsoeVirtIfMessageDigestKey_Object((1,3,6,1,4,1,45,5,14,1,6,1,5),_BsoeVirtIfMessageDigestKey_Type())
bsoeVirtIfMessageDigestKey.setMaxAccess(_F)
if mibBuilder.loadTexts:bsoeVirtIfMessageDigestKey.setStatus(_A)
_BsoeVirtIfMessageDigestRowStatus_Type=RowStatus
_BsoeVirtIfMessageDigestRowStatus_Object=MibTableColumn
bsoeVirtIfMessageDigestRowStatus=_BsoeVirtIfMessageDigestRowStatus_Object((1,3,6,1,4,1,45,5,14,1,6,1,6),_BsoeVirtIfMessageDigestRowStatus_Type())
bsoeVirtIfMessageDigestRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:bsoeVirtIfMessageDigestRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'bayStackOspfExtMib':bayStackOspfExtMib,'bsoeNotifications':bsoeNotifications,'bsoeObjects':bsoeObjects,'bsoeScalars':bsoeScalars,'bsoeApplyRedistribute':bsoeApplyRedistribute,'bsoeHardwareCompatibilityMode':bsoeHardwareCompatibilityMode,'bsoeOspfIfExtTable':bsoeOspfIfExtTable,'bsoeOspfIfExtEntry':bsoeOspfIfExtEntry,_J:bsoeOspfIfIpAddress,_K:bsoeOspfAddressLessIf,'bsoeOspfIfExtAdvertiseWhenDown':bsoeOspfIfExtAdvertiseWhenDown,'bsoeOspfIfExtPrimaryMd5Key':bsoeOspfIfExtPrimaryMd5Key,'bsoeOspfIfExtMtuIgnore':bsoeOspfIfExtMtuIgnore,'bsoeOspfIfExtType':bsoeOspfIfExtType,'bsoeMessageDigestTable':bsoeMessageDigestTable,'bsoeMessageDigestEntry':bsoeMessageDigestEntry,_L:bsoeMessageDigestIpAddress,_M:bsoeMessageDigestAddressLessIf,_N:bsoeMessageDigestIndex,_O:bsoeMessageDigestType,'bsoeMessageDigestKey':bsoeMessageDigestKey,'bsoeMessageDigestRowStatus':bsoeMessageDigestRowStatus,'bsoeOspfNbrExtTable':bsoeOspfNbrExtTable,'bsoeOspfNbrExtEntry':bsoeOspfNbrExtEntry,_P:bsoeOspfNbrExtIpAddr,_Q:bsoeOspfNbrExtAddressLessIndex,'bsoeOspfNbrExtInterfaceAddr':bsoeOspfNbrExtInterfaceAddr,'bsoeOspfNbrExtAdjacencyErrorCode':bsoeOspfNbrExtAdjacencyErrorCode,'bsoeOspfVirtIfExtTable':bsoeOspfVirtIfExtTable,'bsoeOspfVirtIfExtEntry':bsoeOspfVirtIfExtEntry,_R:bsoeOspfVirtIfExtAreaId,_S:bsoeOspfVirtIfExtNeighbor,'bsoeOspfVirtIfExtPrimaryMd5Key':bsoeOspfVirtIfExtPrimaryMd5Key,'bsoeOspfVirtIfExtType':bsoeOspfVirtIfExtType,'bsoeVirtIfMessageDigestTable':bsoeVirtIfMessageDigestTable,'bsoeVirtIfMessageDigestEntry':bsoeVirtIfMessageDigestEntry,_T:bsoeVirtIfMessageDigestAreaId,_U:bsoeVirtIfMessageDigestNeighbor,_V:bsoeVirtIfMessageDigestIndex,_W:bsoeVirtIfMessageDigestType,'bsoeVirtIfMessageDigestKey':bsoeVirtIfMessageDigestKey,'bsoeVirtIfMessageDigestRowStatus':bsoeVirtIfMessageDigestRowStatus})