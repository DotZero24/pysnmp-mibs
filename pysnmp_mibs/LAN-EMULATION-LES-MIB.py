_V='lesErrLogIndex'
_U='TruthValue'
_T='lesLeArpRdBridgeNum'
_S='lesLeArpRdSegId'
_R='lesLeArpMacAddr'
_Q='lesBusConfIndex'
_P='lesVccCtlDistVci'
_O='lesVccCtlDistVpi'
_N='lesVccAtmIfIndex'
_M='DisplayString'
_L='AtmLaneMask'
_K='Integer'
_J='lesLecIndex'
_I='other'
_H='LeArpTableEntryType'
_G='not-accessible'
_F='lesConfIndex'
_E='Integer32'
_D='LAN-EMULATION-LES-MIB'
_C='read-write'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1',_K,'OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
LeArpTableEntryType,VciInteger,VpiInteger,atmfLanEmulation=mibBuilder.importSymbols('LAN-EMULATION-CLIENT-MIB',_H,'VciInteger','VpiInteger','atmfLanEmulation')
AtmLaneMask,IfIndexOrZero,Integer,TIMESTAMP=mibBuilder.importSymbols('LAN-EMULATION-ELAN-MIB',_L,'IfIndexOrZero',_K,'TIMESTAMP')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_M,'PhysAddress','TextualConvention')
class TruthValue(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
class RowStatus(Integer32):0
class AtmLaneAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(20,20))
class MacAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
class LesLecDataFrameFormat(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('aflane8023',2),('aflane8025',3)))
class LesLecDataFrameSize(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5)));namedValues=NamedValues(*(('max1516',2),('max4544',3),('max9234',4),('max18190',5)))
_LesMIB_ObjectIdentity=ObjectIdentity
lesMIB=_LesMIB_ObjectIdentity((1,3,6,1,4,1,353,5,3,3))
_LesConfGroup_ObjectIdentity=ObjectIdentity
lesConfGroup=_LesConfGroup_ObjectIdentity((1,3,6,1,4,1,353,5,3,3,1))
_LesConfNextId_Type=Integer32
_LesConfNextId_Object=MibScalar
lesConfNextId=_LesConfNextId_Object((1,3,6,1,4,1,353,5,3,3,1,1),_LesConfNextId_Type())
lesConfNextId.setMaxAccess(_B)
if mibBuilder.loadTexts:lesConfNextId.setStatus(_A)
_LesConfTable_Object=MibTable
lesConfTable=_LesConfTable_Object((1,3,6,1,4,1,353,5,3,3,1,2))
if mibBuilder.loadTexts:lesConfTable.setStatus(_A)
_LesConfEntry_Object=MibTableRow
lesConfEntry=_LesConfEntry_Object((1,3,6,1,4,1,353,5,3,3,1,2,1))
lesConfEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:lesConfEntry.setStatus(_A)
_LesConfIndex_Type=Integer32
_LesConfIndex_Object=MibTableColumn
lesConfIndex=_LesConfIndex_Object((1,3,6,1,4,1,353,5,3,3,1,2,1,1),_LesConfIndex_Type())
lesConfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:lesConfIndex.setStatus(_A)
_LesAtmAddrSpec_Type=AtmLaneAddress
_LesAtmAddrSpec_Object=MibTableColumn
lesAtmAddrSpec=_LesAtmAddrSpec_Object((1,3,6,1,4,1,353,5,3,3,1,2,1,2),_LesAtmAddrSpec_Type())
lesAtmAddrSpec.setMaxAccess(_C)
if mibBuilder.loadTexts:lesAtmAddrSpec.setStatus(_A)
class _LesAtmAddrMask_Type(AtmLaneMask):defaultHexValue='FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'
_LesAtmAddrMask_Type.__name__=_L
_LesAtmAddrMask_Object=MibTableColumn
lesAtmAddrMask=_LesAtmAddrMask_Object((1,3,6,1,4,1,353,5,3,3,1,2,1,3),_LesAtmAddrMask_Type())
lesAtmAddrMask.setMaxAccess(_C)
if mibBuilder.loadTexts:lesAtmAddrMask.setStatus(_A)
_LesAtmAddrActual_Type=AtmLaneAddress
_LesAtmAddrActual_Object=MibTableColumn
lesAtmAddrActual=_LesAtmAddrActual_Object((1,3,6,1,4,1,353,5,3,3,1,2,1,4),_LesAtmAddrActual_Type())
lesAtmAddrActual.setMaxAccess(_B)
if mibBuilder.loadTexts:lesAtmAddrActual.setStatus(_A)
class _LesElanName_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_LesElanName_Type.__name__=_M
_LesElanName_Object=MibTableColumn
lesElanName=_LesElanName_Object((1,3,6,1,4,1,353,5,3,3,1,2,1,5),_LesElanName_Type())
lesElanName.setMaxAccess(_C)
if mibBuilder.loadTexts:lesElanName.setStatus(_A)
_LesLanType_Type=LesLecDataFrameFormat
_LesLanType_Object=MibTableColumn
lesLanType=_LesLanType_Object((1,3,6,1,4,1,353,5,3,3,1,2,1,6),_LesLanType_Type())
lesLanType.setMaxAccess(_C)
if mibBuilder.loadTexts:lesLanType.setStatus(_A)
_LesLastChange_Type=TIMESTAMP
_LesLastChange_Object=MibTableColumn
lesLastChange=_LesLastChange_Object((1,3,6,1,4,1,353,5,3,3,1,2,1,7),_LesLastChange_Type())
lesLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:lesLastChange.setStatus(_A)
_LesMaxFrameSize_Type=LesLecDataFrameSize
_LesMaxFrameSize_Object=MibTableColumn
lesMaxFrameSize=_LesMaxFrameSize_Object((1,3,6,1,4,1,353,5,3,3,1,2,1,8),_LesMaxFrameSize_Type())
lesMaxFrameSize.setMaxAccess(_C)
if mibBuilder.loadTexts:lesMaxFrameSize.setStatus(_A)
class _LesControlTimeOut_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,300))
_LesControlTimeOut_Type.__name__=_E
_LesControlTimeOut_Object=MibTableColumn
lesControlTimeOut=_LesControlTimeOut_Object((1,3,6,1,4,1,353,5,3,3,1,2,1,9),_LesControlTimeOut_Type())
lesControlTimeOut.setMaxAccess(_C)
if mibBuilder.loadTexts:lesControlTimeOut.setStatus(_A)
class _LesOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),('up',2),('down',3)))
_LesOperStatus_Type.__name__=_E
_LesOperStatus_Object=MibTableColumn
lesOperStatus=_LesOperStatus_Object((1,3,6,1,4,1,353,5,3,3,1,2,1,11),_LesOperStatus_Type())
lesOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:lesOperStatus.setStatus(_A)
class _LesAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('up',2),('down',3)))
_LesAdminStatus_Type.__name__=_E
_LesAdminStatus_Object=MibTableColumn
lesAdminStatus=_LesAdminStatus_Object((1,3,6,1,4,1,353,5,3,3,1,2,1,12),_LesAdminStatus_Type())
lesAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:lesAdminStatus.setStatus(_A)
_LesRowStatus_Type=RowStatus
_LesRowStatus_Object=MibTableColumn
lesRowStatus=_LesRowStatus_Object((1,3,6,1,4,1,353,5,3,3,1,2,1,13),_LesRowStatus_Type())
lesRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:lesRowStatus.setStatus(_A)
_LesVccTable_Object=MibTable
lesVccTable=_LesVccTable_Object((1,3,6,1,4,1,353,5,3,3,1,3))
if mibBuilder.loadTexts:lesVccTable.setStatus(_A)
_LesVccEntry_Object=MibTableRow
lesVccEntry=_LesVccEntry_Object((1,3,6,1,4,1,353,5,3,3,1,3,1))
lesVccEntry.setIndexNames((0,_D,_F),(0,_D,_N),(0,_D,_O),(0,_D,_P))
if mibBuilder.loadTexts:lesVccEntry.setStatus(_A)
_LesVccAtmIfIndex_Type=IfIndexOrZero
_LesVccAtmIfIndex_Object=MibTableColumn
lesVccAtmIfIndex=_LesVccAtmIfIndex_Object((1,3,6,1,4,1,353,5,3,3,1,3,1,1),_LesVccAtmIfIndex_Type())
lesVccAtmIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:lesVccAtmIfIndex.setStatus(_A)
_LesVccCtlDistVpi_Type=VpiInteger
_LesVccCtlDistVpi_Object=MibTableColumn
lesVccCtlDistVpi=_LesVccCtlDistVpi_Object((1,3,6,1,4,1,353,5,3,3,1,3,1,2),_LesVccCtlDistVpi_Type())
lesVccCtlDistVpi.setMaxAccess(_G)
if mibBuilder.loadTexts:lesVccCtlDistVpi.setStatus(_A)
_LesVccCtlDistVci_Type=VciInteger
_LesVccCtlDistVci_Object=MibTableColumn
lesVccCtlDistVci=_LesVccCtlDistVci_Object((1,3,6,1,4,1,353,5,3,3,1,3,1,3),_LesVccCtlDistVci_Type())
lesVccCtlDistVci.setMaxAccess(_G)
if mibBuilder.loadTexts:lesVccCtlDistVci.setStatus(_A)
_LesVccRowStatus_Type=RowStatus
_LesVccRowStatus_Object=MibTableColumn
lesVccRowStatus=_LesVccRowStatus_Object((1,3,6,1,4,1,353,5,3,3,1,3,1,4),_LesVccRowStatus_Type())
lesVccRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:lesVccRowStatus.setStatus(_A)
_LesBusTable_Object=MibTable
lesBusTable=_LesBusTable_Object((1,3,6,1,4,1,353,5,3,3,1,4))
if mibBuilder.loadTexts:lesBusTable.setStatus(_A)
_LesBusEntry_Object=MibTableRow
lesBusEntry=_LesBusEntry_Object((1,3,6,1,4,1,353,5,3,3,1,4,1))
lesBusEntry.setIndexNames((0,_D,_F),(0,_D,_Q))
if mibBuilder.loadTexts:lesBusEntry.setStatus(_A)
_LesBusConfIndex_Type=Integer32
_LesBusConfIndex_Object=MibTableColumn
lesBusConfIndex=_LesBusConfIndex_Object((1,3,6,1,4,1,353,5,3,3,1,4,1,1),_LesBusConfIndex_Type())
lesBusConfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:lesBusConfIndex.setStatus(_A)
_LesBusAddress_Type=AtmLaneAddress
_LesBusAddress_Object=MibTableColumn
lesBusAddress=_LesBusAddress_Object((1,3,6,1,4,1,353,5,3,3,1,4,1,2),_LesBusAddress_Type())
lesBusAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:lesBusAddress.setStatus(_A)
_LesLeArpMacTable_Object=MibTable
lesLeArpMacTable=_LesLeArpMacTable_Object((1,3,6,1,4,1,353,5,3,3,1,5))
if mibBuilder.loadTexts:lesLeArpMacTable.setStatus(_A)
_LesLeArpMacEntry_Object=MibTableRow
lesLeArpMacEntry=_LesLeArpMacEntry_Object((1,3,6,1,4,1,353,5,3,3,1,5,1))
lesLeArpMacEntry.setIndexNames((0,_D,_F),(0,_D,_R))
if mibBuilder.loadTexts:lesLeArpMacEntry.setStatus(_A)
_LesLeArpMacAddr_Type=MacAddress
_LesLeArpMacAddr_Object=MibTableColumn
lesLeArpMacAddr=_LesLeArpMacAddr_Object((1,3,6,1,4,1,353,5,3,3,1,5,1,1),_LesLeArpMacAddr_Type())
lesLeArpMacAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:lesLeArpMacAddr.setStatus(_A)
class _LesLeArpLecId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65279))
_LesLeArpLecId_Type.__name__=_E
_LesLeArpLecId_Object=MibTableColumn
lesLeArpLecId=_LesLeArpLecId_Object((1,3,6,1,4,1,353,5,3,3,1,5,1,2),_LesLeArpLecId_Type())
lesLeArpLecId.setMaxAccess(_B)
if mibBuilder.loadTexts:lesLeArpLecId.setStatus(_A)
_LesLeArpAtmAddr_Type=AtmLaneAddress
_LesLeArpAtmAddr_Object=MibTableColumn
lesLeArpAtmAddr=_LesLeArpAtmAddr_Object((1,3,6,1,4,1,353,5,3,3,1,5,1,3),_LesLeArpAtmAddr_Type())
lesLeArpAtmAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:lesLeArpAtmAddr.setStatus(_A)
class _LesLeArpEntryType_Type(LeArpTableEntryType):defaultValue=4
_LesLeArpEntryType_Type.__name__=_H
_LesLeArpEntryType_Object=MibTableColumn
lesLeArpEntryType=_LesLeArpEntryType_Object((1,3,6,1,4,1,353,5,3,3,1,5,1,4),_LesLeArpEntryType_Type())
lesLeArpEntryType.setMaxAccess(_C)
if mibBuilder.loadTexts:lesLeArpEntryType.setStatus(_A)
_LesLeArpRowStatus_Type=RowStatus
_LesLeArpRowStatus_Object=MibTableColumn
lesLeArpRowStatus=_LesLeArpRowStatus_Object((1,3,6,1,4,1,353,5,3,3,1,5,1,5),_LesLeArpRowStatus_Type())
lesLeArpRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:lesLeArpRowStatus.setStatus(_A)
_LesLeArpRdTable_Object=MibTable
lesLeArpRdTable=_LesLeArpRdTable_Object((1,3,6,1,4,1,353,5,3,3,1,6))
if mibBuilder.loadTexts:lesLeArpRdTable.setStatus(_A)
_LesLeArpRdEntry_Object=MibTableRow
lesLeArpRdEntry=_LesLeArpRdEntry_Object((1,3,6,1,4,1,353,5,3,3,1,6,1))
lesLeArpRdEntry.setIndexNames((0,_D,_F),(0,_D,_S),(0,_D,_T))
if mibBuilder.loadTexts:lesLeArpRdEntry.setStatus(_A)
class _LesLeArpRdSegId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_LesLeArpRdSegId_Type.__name__=_E
_LesLeArpRdSegId_Object=MibTableColumn
lesLeArpRdSegId=_LesLeArpRdSegId_Object((1,3,6,1,4,1,353,5,3,3,1,6,1,1),_LesLeArpRdSegId_Type())
lesLeArpRdSegId.setMaxAccess(_G)
if mibBuilder.loadTexts:lesLeArpRdSegId.setStatus(_A)
class _LesLeArpRdBridgeNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_LesLeArpRdBridgeNum_Type.__name__=_E
_LesLeArpRdBridgeNum_Object=MibTableColumn
lesLeArpRdBridgeNum=_LesLeArpRdBridgeNum_Object((1,3,6,1,4,1,353,5,3,3,1,6,1,2),_LesLeArpRdBridgeNum_Type())
lesLeArpRdBridgeNum.setMaxAccess(_G)
if mibBuilder.loadTexts:lesLeArpRdBridgeNum.setStatus(_A)
class _LesLeArpRdLecId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65279))
_LesLeArpRdLecId_Type.__name__=_E
_LesLeArpRdLecId_Object=MibTableColumn
lesLeArpRdLecId=_LesLeArpRdLecId_Object((1,3,6,1,4,1,353,5,3,3,1,6,1,3),_LesLeArpRdLecId_Type())
lesLeArpRdLecId.setMaxAccess(_B)
if mibBuilder.loadTexts:lesLeArpRdLecId.setStatus(_A)
_LesLeArpRdAtmAddr_Type=AtmLaneAddress
_LesLeArpRdAtmAddr_Object=MibTableColumn
lesLeArpRdAtmAddr=_LesLeArpRdAtmAddr_Object((1,3,6,1,4,1,353,5,3,3,1,6,1,4),_LesLeArpRdAtmAddr_Type())
lesLeArpRdAtmAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:lesLeArpRdAtmAddr.setStatus(_A)
class _LesLeArpRdEntryType_Type(LeArpTableEntryType):defaultValue=4
_LesLeArpRdEntryType_Type.__name__=_H
_LesLeArpRdEntryType_Object=MibTableColumn
lesLeArpRdEntryType=_LesLeArpRdEntryType_Object((1,3,6,1,4,1,353,5,3,3,1,6,1,5),_LesLeArpRdEntryType_Type())
lesLeArpRdEntryType.setMaxAccess(_C)
if mibBuilder.loadTexts:lesLeArpRdEntryType.setStatus(_A)
_LesLeArpRdRowStatus_Type=RowStatus
_LesLeArpRdRowStatus_Object=MibTableColumn
lesLeArpRdRowStatus=_LesLeArpRdRowStatus_Object((1,3,6,1,4,1,353,5,3,3,1,6,1,6),_LesLeArpRdRowStatus_Type())
lesLeArpRdRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:lesLeArpRdRowStatus.setStatus(_A)
_LesLecTableLastChange_Type=TIMESTAMP
_LesLecTableLastChange_Object=MibScalar
lesLecTableLastChange=_LesLecTableLastChange_Object((1,3,6,1,4,1,353,5,3,3,1,7),_LesLecTableLastChange_Type())
lesLecTableLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:lesLecTableLastChange.setStatus(_A)
_LesLecTable_Object=MibTable
lesLecTable=_LesLecTable_Object((1,3,6,1,4,1,353,5,3,3,1,8))
if mibBuilder.loadTexts:lesLecTable.setStatus(_A)
_LesLecEntry_Object=MibTableRow
lesLecEntry=_LesLecEntry_Object((1,3,6,1,4,1,353,5,3,3,1,8,1))
lesLecEntry.setIndexNames((0,_D,_F),(0,_D,_J))
if mibBuilder.loadTexts:lesLecEntry.setStatus(_A)
class _LesLecIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_LesLecIndex_Type.__name__=_E
_LesLecIndex_Object=MibTableColumn
lesLecIndex=_LesLecIndex_Object((1,3,6,1,4,1,353,5,3,3,1,8,1,1),_LesLecIndex_Type())
lesLecIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:lesLecIndex.setStatus(_A)
_LesLecAtmAddr_Type=AtmLaneAddress
_LesLecAtmAddr_Object=MibTableColumn
lesLecAtmAddr=_LesLecAtmAddr_Object((1,3,6,1,4,1,353,5,3,3,1,8,1,2),_LesLecAtmAddr_Type())
lesLecAtmAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:lesLecAtmAddr.setStatus(_A)
class _LesLecProxy_Type(TruthValue):defaultValue=2
_LesLecProxy_Type.__name__=_U
_LesLecProxy_Object=MibTableColumn
lesLecProxy=_LesLecProxy_Object((1,3,6,1,4,1,353,5,3,3,1,8,1,3),_LesLecProxy_Type())
lesLecProxy.setMaxAccess(_B)
if mibBuilder.loadTexts:lesLecProxy.setStatus(_A)
class _LesLecId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65279))
_LesLecId_Type.__name__=_E
_LesLecId_Object=MibTableColumn
lesLecId=_LesLecId_Object((1,3,6,1,4,1,353,5,3,3,1,8,1,4),_LesLecId_Type())
lesLecId.setMaxAccess(_B)
if mibBuilder.loadTexts:lesLecId.setStatus(_A)
_LesLecAtmIfIndex_Type=IfIndexOrZero
_LesLecAtmIfIndex_Object=MibTableColumn
lesLecAtmIfIndex=_LesLecAtmIfIndex_Object((1,3,6,1,4,1,353,5,3,3,1,8,1,5),_LesLecAtmIfIndex_Type())
lesLecAtmIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:lesLecAtmIfIndex.setStatus(_A)
_LesLecCtlDirectVpi_Type=VpiInteger
_LesLecCtlDirectVpi_Object=MibTableColumn
lesLecCtlDirectVpi=_LesLecCtlDirectVpi_Object((1,3,6,1,4,1,353,5,3,3,1,8,1,6),_LesLecCtlDirectVpi_Type())
lesLecCtlDirectVpi.setMaxAccess(_C)
if mibBuilder.loadTexts:lesLecCtlDirectVpi.setStatus(_A)
_LesLecCtlDirectVci_Type=VciInteger
_LesLecCtlDirectVci_Object=MibTableColumn
lesLecCtlDirectVci=_LesLecCtlDirectVci_Object((1,3,6,1,4,1,353,5,3,3,1,8,1,7),_LesLecCtlDirectVci_Type())
lesLecCtlDirectVci.setMaxAccess(_C)
if mibBuilder.loadTexts:lesLecCtlDirectVci.setStatus(_A)
_LesLecLastChange_Type=TIMESTAMP
_LesLecLastChange_Object=MibTableColumn
lesLecLastChange=_LesLecLastChange_Object((1,3,6,1,4,1,353,5,3,3,1,8,1,8),_LesLecLastChange_Type())
lesLecLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:lesLecLastChange.setStatus(_A)
class _LesLecState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_I,1),('noLesConnect',2),('lesConnect',3),('joining',4),('addLec',5),('joinedLes',6)))
_LesLecState_Type.__name__=_E
_LesLecState_Object=MibTableColumn
lesLecState=_LesLecState_Object((1,3,6,1,4,1,353,5,3,3,1,8,1,9),_LesLecState_Type())
lesLecState.setMaxAccess(_B)
if mibBuilder.loadTexts:lesLecState.setStatus(_A)
_LesLecRowStatus_Type=RowStatus
_LesLecRowStatus_Object=MibTableColumn
lesLecRowStatus=_LesLecRowStatus_Object((1,3,6,1,4,1,353,5,3,3,1,8,1,10),_LesLecRowStatus_Type())
lesLecRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:lesLecRowStatus.setStatus(_A)
_LesStatGroup_ObjectIdentity=ObjectIdentity
lesStatGroup=_LesStatGroup_ObjectIdentity((1,3,6,1,4,1,353,5,3,3,2))
_LesStatTable_Object=MibTable
lesStatTable=_LesStatTable_Object((1,3,6,1,4,1,353,5,3,3,2,1))
if mibBuilder.loadTexts:lesStatTable.setStatus(_A)
_LesStatEntry_Object=MibTableRow
lesStatEntry=_LesStatEntry_Object((1,3,6,1,4,1,353,5,3,3,2,1,1))
lesStatEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:lesStatEntry.setStatus(_A)
_LesStatJoinOk_Type=Counter32
_LesStatJoinOk_Object=MibTableColumn
lesStatJoinOk=_LesStatJoinOk_Object((1,3,6,1,4,1,353,5,3,3,2,1,1,1),_LesStatJoinOk_Type())
lesStatJoinOk.setMaxAccess(_B)
if mibBuilder.loadTexts:lesStatJoinOk.setStatus(_A)
_LesStatVerNotSup_Type=Counter32
_LesStatVerNotSup_Object=MibTableColumn
lesStatVerNotSup=_LesStatVerNotSup_Object((1,3,6,1,4,1,353,5,3,3,2,1,1,2),_LesStatVerNotSup_Type())
lesStatVerNotSup.setMaxAccess(_B)
if mibBuilder.loadTexts:lesStatVerNotSup.setStatus(_A)
_LesStatInvalidReqParam_Type=Counter32
_LesStatInvalidReqParam_Object=MibTableColumn
lesStatInvalidReqParam=_LesStatInvalidReqParam_Object((1,3,6,1,4,1,353,5,3,3,2,1,1,3),_LesStatInvalidReqParam_Type())
lesStatInvalidReqParam.setMaxAccess(_B)
if mibBuilder.loadTexts:lesStatInvalidReqParam.setStatus(_A)
_LesStatDupLanDest_Type=Counter32
_LesStatDupLanDest_Object=MibTableColumn
lesStatDupLanDest=_LesStatDupLanDest_Object((1,3,6,1,4,1,353,5,3,3,2,1,1,4),_LesStatDupLanDest_Type())
lesStatDupLanDest.setMaxAccess(_B)
if mibBuilder.loadTexts:lesStatDupLanDest.setStatus(_A)
_LesStatDupAtmAddr_Type=Counter32
_LesStatDupAtmAddr_Object=MibTableColumn
lesStatDupAtmAddr=_LesStatDupAtmAddr_Object((1,3,6,1,4,1,353,5,3,3,2,1,1,5),_LesStatDupAtmAddr_Type())
lesStatDupAtmAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:lesStatDupAtmAddr.setStatus(_A)
_LesStatInsRes_Type=Counter32
_LesStatInsRes_Object=MibTableColumn
lesStatInsRes=_LesStatInsRes_Object((1,3,6,1,4,1,353,5,3,3,2,1,1,6),_LesStatInsRes_Type())
lesStatInsRes.setMaxAccess(_B)
if mibBuilder.loadTexts:lesStatInsRes.setStatus(_A)
_LesStatAccDenied_Type=Counter32
_LesStatAccDenied_Object=MibTableColumn
lesStatAccDenied=_LesStatAccDenied_Object((1,3,6,1,4,1,353,5,3,3,2,1,1,7),_LesStatAccDenied_Type())
lesStatAccDenied.setMaxAccess(_B)
if mibBuilder.loadTexts:lesStatAccDenied.setStatus(_A)
_LesStatInvalidReqId_Type=Counter32
_LesStatInvalidReqId_Object=MibTableColumn
lesStatInvalidReqId=_LesStatInvalidReqId_Object((1,3,6,1,4,1,353,5,3,3,2,1,1,8),_LesStatInvalidReqId_Type())
lesStatInvalidReqId.setMaxAccess(_B)
if mibBuilder.loadTexts:lesStatInvalidReqId.setStatus(_A)
_LesStatInvalidLanDest_Type=Counter32
_LesStatInvalidLanDest_Object=MibTableColumn
lesStatInvalidLanDest=_LesStatInvalidLanDest_Object((1,3,6,1,4,1,353,5,3,3,2,1,1,9),_LesStatInvalidLanDest_Type())
lesStatInvalidLanDest.setMaxAccess(_B)
if mibBuilder.loadTexts:lesStatInvalidLanDest.setStatus(_A)
_LesStatInvalidAtmAddr_Type=Counter32
_LesStatInvalidAtmAddr_Object=MibTableColumn
lesStatInvalidAtmAddr=_LesStatInvalidAtmAddr_Object((1,3,6,1,4,1,353,5,3,3,2,1,1,10),_LesStatInvalidAtmAddr_Type())
lesStatInvalidAtmAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:lesStatInvalidAtmAddr.setStatus(_A)
_LesStatInBadPkts_Type=Counter32
_LesStatInBadPkts_Object=MibTableColumn
lesStatInBadPkts=_LesStatInBadPkts_Object((1,3,6,1,4,1,353,5,3,3,2,1,1,11),_LesStatInBadPkts_Type())
lesStatInBadPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:lesStatInBadPkts.setStatus(_A)
_LesStatOutRegFails_Type=Counter32
_LesStatOutRegFails_Object=MibTableColumn
lesStatOutRegFails=_LesStatOutRegFails_Object((1,3,6,1,4,1,353,5,3,3,2,1,1,12),_LesStatOutRegFails_Type())
lesStatOutRegFails.setMaxAccess(_B)
if mibBuilder.loadTexts:lesStatOutRegFails.setStatus(_A)
_LesStatLeArpIn_Type=Counter32
_LesStatLeArpIn_Object=MibTableColumn
lesStatLeArpIn=_LesStatLeArpIn_Object((1,3,6,1,4,1,353,5,3,3,2,1,1,13),_LesStatLeArpIn_Type())
lesStatLeArpIn.setMaxAccess(_B)
if mibBuilder.loadTexts:lesStatLeArpIn.setStatus(_A)
_LesStatLeArpFwd_Type=Counter32
_LesStatLeArpFwd_Object=MibTableColumn
lesStatLeArpFwd=_LesStatLeArpFwd_Object((1,3,6,1,4,1,353,5,3,3,2,1,1,14),_LesStatLeArpFwd_Type())
lesStatLeArpFwd.setMaxAccess(_B)
if mibBuilder.loadTexts:lesStatLeArpFwd.setStatus(_A)
_LesLecStatGroup_ObjectIdentity=ObjectIdentity
lesLecStatGroup=_LesLecStatGroup_ObjectIdentity((1,3,6,1,4,1,353,5,3,3,3))
_LesLecStatTable_Object=MibTable
lesLecStatTable=_LesLecStatTable_Object((1,3,6,1,4,1,353,5,3,3,3,1))
if mibBuilder.loadTexts:lesLecStatTable.setStatus(_A)
_LesLecStatEntry_Object=MibTableRow
lesLecStatEntry=_LesLecStatEntry_Object((1,3,6,1,4,1,353,5,3,3,3,1,1))
lesLecStatEntry.setIndexNames((0,_D,_F),(0,_D,_J))
if mibBuilder.loadTexts:lesLecStatEntry.setStatus(_A)
_LesLecRecvs_Type=Counter32
_LesLecRecvs_Object=MibTableColumn
lesLecRecvs=_LesLecRecvs_Object((1,3,6,1,4,1,353,5,3,3,3,1,1,1),_LesLecRecvs_Type())
lesLecRecvs.setMaxAccess(_B)
if mibBuilder.loadTexts:lesLecRecvs.setStatus(_A)
_LesLecSends_Type=Counter32
_LesLecSends_Object=MibTableColumn
lesLecSends=_LesLecSends_Object((1,3,6,1,4,1,353,5,3,3,3,1,1,3),_LesLecSends_Type())
lesLecSends.setMaxAccess(_B)
if mibBuilder.loadTexts:lesLecSends.setStatus(_A)
_LesLecInRegReq_Type=Counter32
_LesLecInRegReq_Object=MibTableColumn
lesLecInRegReq=_LesLecInRegReq_Object((1,3,6,1,4,1,353,5,3,3,3,1,1,4),_LesLecInRegReq_Type())
lesLecInRegReq.setMaxAccess(_B)
if mibBuilder.loadTexts:lesLecInRegReq.setStatus(_A)
_LesLecInUnReg_Type=Counter32
_LesLecInUnReg_Object=MibTableColumn
lesLecInUnReg=_LesLecInUnReg_Object((1,3,6,1,4,1,353,5,3,3,3,1,1,5),_LesLecInUnReg_Type())
lesLecInUnReg.setMaxAccess(_B)
if mibBuilder.loadTexts:lesLecInUnReg.setStatus(_A)
_LesLecInLeArpUcast_Type=Counter32
_LesLecInLeArpUcast_Object=MibTableColumn
lesLecInLeArpUcast=_LesLecInLeArpUcast_Object((1,3,6,1,4,1,353,5,3,3,3,1,1,6),_LesLecInLeArpUcast_Type())
lesLecInLeArpUcast.setMaxAccess(_B)
if mibBuilder.loadTexts:lesLecInLeArpUcast.setStatus(_A)
_LesLecInLeArpBcast_Type=Counter32
_LesLecInLeArpBcast_Object=MibTableColumn
lesLecInLeArpBcast=_LesLecInLeArpBcast_Object((1,3,6,1,4,1,353,5,3,3,3,1,1,7),_LesLecInLeArpBcast_Type())
lesLecInLeArpBcast.setMaxAccess(_B)
if mibBuilder.loadTexts:lesLecInLeArpBcast.setStatus(_A)
_LesLecInLeArpResp_Type=Counter32
_LesLecInLeArpResp_Object=MibTableColumn
lesLecInLeArpResp=_LesLecInLeArpResp_Object((1,3,6,1,4,1,353,5,3,3,3,1,1,8),_LesLecInLeArpResp_Type())
lesLecInLeArpResp.setMaxAccess(_B)
if mibBuilder.loadTexts:lesLecInLeArpResp.setStatus(_A)
_LesLecInNArp_Type=Counter32
_LesLecInNArp_Object=MibTableColumn
lesLecInNArp=_LesLecInNArp_Object((1,3,6,1,4,1,353,5,3,3,3,1,1,10),_LesLecInNArp_Type())
lesLecInNArp.setMaxAccess(_B)
if mibBuilder.loadTexts:lesLecInNArp.setStatus(_A)
_LesFaultGroup_ObjectIdentity=ObjectIdentity
lesFaultGroup=_LesFaultGroup_ObjectIdentity((1,3,6,1,4,1,353,5,3,3,4))
_LesErrCtlTable_Object=MibTable
lesErrCtlTable=_LesErrCtlTable_Object((1,3,6,1,4,1,353,5,3,3,4,1))
if mibBuilder.loadTexts:lesErrCtlTable.setStatus(_A)
_LesErrCtlEntry_Object=MibTableRow
lesErrCtlEntry=_LesErrCtlEntry_Object((1,3,6,1,4,1,353,5,3,3,4,1,1))
lesErrCtlEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:lesErrCtlEntry.setStatus(_A)
class _LesErrCtlAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_LesErrCtlAdminStatus_Type.__name__=_E
_LesErrCtlAdminStatus_Object=MibTableColumn
lesErrCtlAdminStatus=_LesErrCtlAdminStatus_Object((1,3,6,1,4,1,353,5,3,3,4,1,1,1),_LesErrCtlAdminStatus_Type())
lesErrCtlAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:lesErrCtlAdminStatus.setStatus(_A)
class _LesErrCtlOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_I,1),('active',2),('outOfRes',3),('failed',4),('disabled',5)))
_LesErrCtlOperStatus_Type.__name__=_E
_LesErrCtlOperStatus_Object=MibTableColumn
lesErrCtlOperStatus=_LesErrCtlOperStatus_Object((1,3,6,1,4,1,353,5,3,3,4,1,1,2),_LesErrCtlOperStatus_Type())
lesErrCtlOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:lesErrCtlOperStatus.setStatus(_A)
class _LesErrCtlClearLog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noOp',1),('clear',2)))
_LesErrCtlClearLog_Type.__name__=_E
_LesErrCtlClearLog_Object=MibTableColumn
lesErrCtlClearLog=_LesErrCtlClearLog_Object((1,3,6,1,4,1,353,5,3,3,4,1,1,3),_LesErrCtlClearLog_Type())
lesErrCtlClearLog.setMaxAccess(_C)
if mibBuilder.loadTexts:lesErrCtlClearLog.setStatus(_A)
class _LesErrCtlMaxEntries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_LesErrCtlMaxEntries_Type.__name__=_E
_LesErrCtlMaxEntries_Object=MibTableColumn
lesErrCtlMaxEntries=_LesErrCtlMaxEntries_Object((1,3,6,1,4,1,353,5,3,3,4,1,1,4),_LesErrCtlMaxEntries_Type())
lesErrCtlMaxEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:lesErrCtlMaxEntries.setStatus(_A)
class _LesErrCtlLastEntry_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_LesErrCtlLastEntry_Type.__name__=_E
_LesErrCtlLastEntry_Object=MibTableColumn
lesErrCtlLastEntry=_LesErrCtlLastEntry_Object((1,3,6,1,4,1,353,5,3,3,4,1,1,5),_LesErrCtlLastEntry_Type())
lesErrCtlLastEntry.setMaxAccess(_C)
if mibBuilder.loadTexts:lesErrCtlLastEntry.setStatus(_A)
_LesErrLogTable_Object=MibTable
lesErrLogTable=_LesErrLogTable_Object((1,3,6,1,4,1,353,5,3,3,4,2))
if mibBuilder.loadTexts:lesErrLogTable.setStatus(_A)
_LesErrLogEntry_Object=MibTableRow
lesErrLogEntry=_LesErrLogEntry_Object((1,3,6,1,4,1,353,5,3,3,4,2,1))
lesErrLogEntry.setIndexNames((0,_D,_F),(0,_D,_V))
if mibBuilder.loadTexts:lesErrLogEntry.setStatus(_A)
class _LesErrLogIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_LesErrLogIndex_Type.__name__=_E
_LesErrLogIndex_Object=MibTableColumn
lesErrLogIndex=_LesErrLogIndex_Object((1,3,6,1,4,1,353,5,3,3,4,2,1,1),_LesErrLogIndex_Type())
lesErrLogIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:lesErrLogIndex.setStatus(_A)
_LesErrLogAtmAddr_Type=AtmLaneAddress
_LesErrLogAtmAddr_Object=MibTableColumn
lesErrLogAtmAddr=_LesErrLogAtmAddr_Object((1,3,6,1,4,1,353,5,3,3,4,2,1,2),_LesErrLogAtmAddr_Type())
lesErrLogAtmAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:lesErrLogAtmAddr.setStatus(_A)
class _LesErrLogErrCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,22))
_LesErrLogErrCode_Type.__name__=_E
_LesErrLogErrCode_Object=MibTableColumn
lesErrLogErrCode=_LesErrLogErrCode_Object((1,3,6,1,4,1,353,5,3,3,4,2,1,3),_LesErrLogErrCode_Type())
lesErrLogErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:lesErrLogErrCode.setStatus(_A)
_LesErrLogTime_Type=TIMESTAMP
_LesErrLogTime_Object=MibTableColumn
lesErrLogTime=_LesErrLogTime_Object((1,3,6,1,4,1,353,5,3,3,4,2,1,4),_LesErrLogTime_Type())
lesErrLogTime.setMaxAccess(_B)
if mibBuilder.loadTexts:lesErrLogTime.setStatus(_A)
mibBuilder.exportSymbols(_D,**{_U:TruthValue,'RowStatus':RowStatus,'AtmLaneAddress':AtmLaneAddress,'MacAddress':MacAddress,'LesLecDataFrameFormat':LesLecDataFrameFormat,'LesLecDataFrameSize':LesLecDataFrameSize,'lesMIB':lesMIB,'lesConfGroup':lesConfGroup,'lesConfNextId':lesConfNextId,'lesConfTable':lesConfTable,'lesConfEntry':lesConfEntry,_F:lesConfIndex,'lesAtmAddrSpec':lesAtmAddrSpec,'lesAtmAddrMask':lesAtmAddrMask,'lesAtmAddrActual':lesAtmAddrActual,'lesElanName':lesElanName,'lesLanType':lesLanType,'lesLastChange':lesLastChange,'lesMaxFrameSize':lesMaxFrameSize,'lesControlTimeOut':lesControlTimeOut,'lesOperStatus':lesOperStatus,'lesAdminStatus':lesAdminStatus,'lesRowStatus':lesRowStatus,'lesVccTable':lesVccTable,'lesVccEntry':lesVccEntry,_N:lesVccAtmIfIndex,_O:lesVccCtlDistVpi,_P:lesVccCtlDistVci,'lesVccRowStatus':lesVccRowStatus,'lesBusTable':lesBusTable,'lesBusEntry':lesBusEntry,_Q:lesBusConfIndex,'lesBusAddress':lesBusAddress,'lesLeArpMacTable':lesLeArpMacTable,'lesLeArpMacEntry':lesLeArpMacEntry,_R:lesLeArpMacAddr,'lesLeArpLecId':lesLeArpLecId,'lesLeArpAtmAddr':lesLeArpAtmAddr,'lesLeArpEntryType':lesLeArpEntryType,'lesLeArpRowStatus':lesLeArpRowStatus,'lesLeArpRdTable':lesLeArpRdTable,'lesLeArpRdEntry':lesLeArpRdEntry,_S:lesLeArpRdSegId,_T:lesLeArpRdBridgeNum,'lesLeArpRdLecId':lesLeArpRdLecId,'lesLeArpRdAtmAddr':lesLeArpRdAtmAddr,'lesLeArpRdEntryType':lesLeArpRdEntryType,'lesLeArpRdRowStatus':lesLeArpRdRowStatus,'lesLecTableLastChange':lesLecTableLastChange,'lesLecTable':lesLecTable,'lesLecEntry':lesLecEntry,_J:lesLecIndex,'lesLecAtmAddr':lesLecAtmAddr,'lesLecProxy':lesLecProxy,'lesLecId':lesLecId,'lesLecAtmIfIndex':lesLecAtmIfIndex,'lesLecCtlDirectVpi':lesLecCtlDirectVpi,'lesLecCtlDirectVci':lesLecCtlDirectVci,'lesLecLastChange':lesLecLastChange,'lesLecState':lesLecState,'lesLecRowStatus':lesLecRowStatus,'lesStatGroup':lesStatGroup,'lesStatTable':lesStatTable,'lesStatEntry':lesStatEntry,'lesStatJoinOk':lesStatJoinOk,'lesStatVerNotSup':lesStatVerNotSup,'lesStatInvalidReqParam':lesStatInvalidReqParam,'lesStatDupLanDest':lesStatDupLanDest,'lesStatDupAtmAddr':lesStatDupAtmAddr,'lesStatInsRes':lesStatInsRes,'lesStatAccDenied':lesStatAccDenied,'lesStatInvalidReqId':lesStatInvalidReqId,'lesStatInvalidLanDest':lesStatInvalidLanDest,'lesStatInvalidAtmAddr':lesStatInvalidAtmAddr,'lesStatInBadPkts':lesStatInBadPkts,'lesStatOutRegFails':lesStatOutRegFails,'lesStatLeArpIn':lesStatLeArpIn,'lesStatLeArpFwd':lesStatLeArpFwd,'lesLecStatGroup':lesLecStatGroup,'lesLecStatTable':lesLecStatTable,'lesLecStatEntry':lesLecStatEntry,'lesLecRecvs':lesLecRecvs,'lesLecSends':lesLecSends,'lesLecInRegReq':lesLecInRegReq,'lesLecInUnReg':lesLecInUnReg,'lesLecInLeArpUcast':lesLecInLeArpUcast,'lesLecInLeArpBcast':lesLecInLeArpBcast,'lesLecInLeArpResp':lesLecInLeArpResp,'lesLecInNArp':lesLecInNArp,'lesFaultGroup':lesFaultGroup,'lesErrCtlTable':lesErrCtlTable,'lesErrCtlEntry':lesErrCtlEntry,'lesErrCtlAdminStatus':lesErrCtlAdminStatus,'lesErrCtlOperStatus':lesErrCtlOperStatus,'lesErrCtlClearLog':lesErrCtlClearLog,'lesErrCtlMaxEntries':lesErrCtlMaxEntries,'lesErrCtlLastEntry':lesErrCtlLastEntry,'lesErrLogTable':lesErrLogTable,'lesErrLogEntry':lesErrLogEntry,_V:lesErrLogIndex,'lesErrLogAtmAddr':lesErrLogAtmAddr,'lesErrLogErrCode':lesErrLogErrCode,'lesErrLogTime':lesErrLogTime})