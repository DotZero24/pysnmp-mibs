_P='tnRmdCfmMepDmInitiatorSessionNumber'
_O='tnRmdCfmRemoteMepId'
_N='TruthValue'
_M='Dot1agCfmMaintDomainNameType'
_L='Dot1agCfmMaintDomainName'
_K='not-accessible'
_J='read-write'
_I='read-only'
_H='tnRmdCfmMepNumber'
_G='tnSysSwitchId'
_F='TROPIC-SYSTEM-MIB'
_E='tnRmdSystemId'
_D='TN-RMD-SYSTEM-MIB'
_C='TN-RMD-CFM-MIB'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Dot1agCfmCcmInterval,Dot1agCfmMDLevel,Dot1agCfmMaintAssocName,Dot1agCfmMaintAssocNameType,Dot1agCfmMaintDomainName,Dot1agCfmMaintDomainNameType,Dot1agCfmMepId,Dot1agCfmMpDirection,VlanIdOrNone=mibBuilder.importSymbols('IEEE8021-CFM-MIB','Dot1agCfmCcmInterval','Dot1agCfmMDLevel','Dot1agCfmMaintAssocName','Dot1agCfmMaintAssocNameType',_L,_M,'Dot1agCfmMepId','Dot1agCfmMpDirection','VlanIdOrNone')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_N)
tnRmdSystemId,=mibBuilder.importSymbols(_D,_E)
tnRmdMIBModules,tnRmdObjs=mibBuilder.importSymbols('TROPIC-GLOBAL-REG','tnRmdMIBModules','tnRmdObjs')
tnSysSwitchId,=mibBuilder.importSymbols(_F,_G)
tnRmdCfmMibModule=ModuleIdentity((1,3,6,1,4,1,7483,5,1,4,1))
if mibBuilder.loadTexts:tnRmdCfmMibModule.setRevisions(('2020-11-13 12:00','2020-11-06 12:00','2020-10-09 12:00','2018-02-23 12:00','2016-11-16 00:00','2012-11-28 00:00'))
class TnRmdCfmDmInitiatorSessionMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('cfmDmInitiatorSessionModeNormal',0),('cfmDmInitiatorSessionModeTest',1)))
class TnRmdCfmDmTestMeasurementInterval(TextualConvention,Unsigned32):status=_A
class TnRmdCfmInitiatorSessionState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('cfmInitiatorSessionRunning',0),('cfmInitiatorSessionStopped',1)))
class TnRmdCfmInitiatorSessionType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('cfmInitiatorSessionTypeOnDemand',0),('cfmInitiatorSessionTypeProActive',1)))
class TnRmdCfmMegId(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(48,48));fixedLength=48
class TnRmdCfmMepDefect(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('unl',0),('mmg',1),('unm',2),('loc',3),('rdi',4),('unp',5),('unpr',6)))
class TnRmdCfmMepNumber(TextualConvention,Unsigned32):status=_A
class TnRmdCfmMeasurementInterval(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,3600000))
class IEEE8021PriorityValue(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_TnRmdCfmObjects_ObjectIdentity=ObjectIdentity
tnRmdCfmObjects=_TnRmdCfmObjects_ObjectIdentity((1,3,6,1,4,1,7483,6,4,1,1))
_TnRmdCfmAttributeTotal_Type=Integer32
_TnRmdCfmAttributeTotal_Object=MibScalar
tnRmdCfmAttributeTotal=_TnRmdCfmAttributeTotal_Object((1,3,6,1,4,1,7483,6,4,1,1,1),_TnRmdCfmAttributeTotal_Type())
tnRmdCfmAttributeTotal.setMaxAccess(_I)
if mibBuilder.loadTexts:tnRmdCfmAttributeTotal.setStatus(_A)
_TnRmdSystemCfmTable_Object=MibTable
tnRmdSystemCfmTable=_TnRmdSystemCfmTable_Object((1,3,6,1,4,1,7483,6,4,1,1,2))
if mibBuilder.loadTexts:tnRmdSystemCfmTable.setStatus(_A)
_TnRmdSystemCfmEntry_Object=MibTableRow
tnRmdSystemCfmEntry=_TnRmdSystemCfmEntry_Object((1,3,6,1,4,1,7483,6,4,1,1,2,1))
tnRmdSystemCfmEntry.setIndexNames((0,_F,_G),(0,_D,_E))
if mibBuilder.loadTexts:tnRmdSystemCfmEntry.setStatus(_A)
_TnRmdSystemCfmMaxNrMeps_Type=Unsigned32
_TnRmdSystemCfmMaxNrMeps_Object=MibTableColumn
tnRmdSystemCfmMaxNrMeps=_TnRmdSystemCfmMaxNrMeps_Object((1,3,6,1,4,1,7483,6,4,1,1,2,1,1),_TnRmdSystemCfmMaxNrMeps_Type())
tnRmdSystemCfmMaxNrMeps.setMaxAccess(_I)
if mibBuilder.loadTexts:tnRmdSystemCfmMaxNrMeps.setStatus(_A)
_TnRmdSystemCfmLmMaxNrPriorityLevels_Type=Unsigned32
_TnRmdSystemCfmLmMaxNrPriorityLevels_Object=MibTableColumn
tnRmdSystemCfmLmMaxNrPriorityLevels=_TnRmdSystemCfmLmMaxNrPriorityLevels_Object((1,3,6,1,4,1,7483,6,4,1,1,2,1,2),_TnRmdSystemCfmLmMaxNrPriorityLevels_Type())
tnRmdSystemCfmLmMaxNrPriorityLevels.setMaxAccess(_I)
if mibBuilder.loadTexts:tnRmdSystemCfmLmMaxNrPriorityLevels.setStatus(_A)
_TnRmdSystemCfmDmUpdateLocalTime_Type=TruthValue
_TnRmdSystemCfmDmUpdateLocalTime_Object=MibTableColumn
tnRmdSystemCfmDmUpdateLocalTime=_TnRmdSystemCfmDmUpdateLocalTime_Object((1,3,6,1,4,1,7483,6,4,1,1,2,1,3),_TnRmdSystemCfmDmUpdateLocalTime_Type())
tnRmdSystemCfmDmUpdateLocalTime.setMaxAccess(_J)
if mibBuilder.loadTexts:tnRmdSystemCfmDmUpdateLocalTime.setStatus(_A)
_TnRmdCfmMepTable_Object=MibTable
tnRmdCfmMepTable=_TnRmdCfmMepTable_Object((1,3,6,1,4,1,7483,6,4,1,1,3))
if mibBuilder.loadTexts:tnRmdCfmMepTable.setStatus(_A)
_TnRmdCfmMepEntry_Object=MibTableRow
tnRmdCfmMepEntry=_TnRmdCfmMepEntry_Object((1,3,6,1,4,1,7483,6,4,1,1,3,1))
tnRmdCfmMepEntry.setIndexNames((0,_F,_G),(0,_D,_E),(0,_C,_H))
if mibBuilder.loadTexts:tnRmdCfmMepEntry.setStatus(_A)
_TnRmdCfmMepNumber_Type=TnRmdCfmMepNumber
_TnRmdCfmMepNumber_Object=MibTableColumn
tnRmdCfmMepNumber=_TnRmdCfmMepNumber_Object((1,3,6,1,4,1,7483,6,4,1,1,3,1,1),_TnRmdCfmMepNumber_Type())
tnRmdCfmMepNumber.setMaxAccess(_K)
if mibBuilder.loadTexts:tnRmdCfmMepNumber.setStatus(_A)
_TnRmdCfmMepMdIndex_Type=Unsigned32
_TnRmdCfmMepMdIndex_Object=MibTableColumn
tnRmdCfmMepMdIndex=_TnRmdCfmMepMdIndex_Object((1,3,6,1,4,1,7483,6,4,1,1,3,1,2),_TnRmdCfmMepMdIndex_Type())
tnRmdCfmMepMdIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdCfmMepMdIndex.setStatus(_A)
class _TnRmdCfmMepMdFormat_Type(Dot1agCfmMaintDomainNameType):defaultValue=4
_TnRmdCfmMepMdFormat_Type.__name__=_M
_TnRmdCfmMepMdFormat_Object=MibTableColumn
tnRmdCfmMepMdFormat=_TnRmdCfmMepMdFormat_Object((1,3,6,1,4,1,7483,6,4,1,1,3,1,3),_TnRmdCfmMepMdFormat_Type())
tnRmdCfmMepMdFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdCfmMepMdFormat.setStatus(_A)
class _TnRmdCfmMepMdName_Type(Dot1agCfmMaintDomainName):defaultValue=OctetString('DEFAULT')
_TnRmdCfmMepMdName_Type.__name__=_L
_TnRmdCfmMepMdName_Object=MibTableColumn
tnRmdCfmMepMdName=_TnRmdCfmMepMdName_Object((1,3,6,1,4,1,7483,6,4,1,1,3,1,4),_TnRmdCfmMepMdName_Type())
tnRmdCfmMepMdName.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdCfmMepMdName.setStatus(_A)
_TnRmdCfmMepMaIndex_Type=Unsigned32
_TnRmdCfmMepMaIndex_Object=MibTableColumn
tnRmdCfmMepMaIndex=_TnRmdCfmMepMaIndex_Object((1,3,6,1,4,1,7483,6,4,1,1,3,1,5),_TnRmdCfmMepMaIndex_Type())
tnRmdCfmMepMaIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdCfmMepMaIndex.setStatus(_A)
_TnRmdCfmMepMaNetFormat_Type=Dot1agCfmMaintAssocNameType
_TnRmdCfmMepMaNetFormat_Object=MibTableColumn
tnRmdCfmMepMaNetFormat=_TnRmdCfmMepMaNetFormat_Object((1,3,6,1,4,1,7483,6,4,1,1,3,1,6),_TnRmdCfmMepMaNetFormat_Type())
tnRmdCfmMepMaNetFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdCfmMepMaNetFormat.setStatus(_A)
_TnRmdCfmMepMaNetName_Type=Dot1agCfmMaintAssocName
_TnRmdCfmMepMaNetName_Object=MibTableColumn
tnRmdCfmMepMaNetName=_TnRmdCfmMepMaNetName_Object((1,3,6,1,4,1,7483,6,4,1,1,3,1,7),_TnRmdCfmMepMaNetName_Type())
tnRmdCfmMepMaNetName.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdCfmMepMaNetName.setStatus(_A)
_TnRmdCfmMepMdLevel_Type=Dot1agCfmMDLevel
_TnRmdCfmMepMdLevel_Object=MibTableColumn
tnRmdCfmMepMdLevel=_TnRmdCfmMepMdLevel_Object((1,3,6,1,4,1,7483,6,4,1,1,3,1,8),_TnRmdCfmMepMdLevel_Type())
tnRmdCfmMepMdLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdCfmMepMdLevel.setStatus(_A)
_TnRmdCfmMepMegId_Type=TnRmdCfmMegId
_TnRmdCfmMepMegId_Object=MibTableColumn
tnRmdCfmMepMegId=_TnRmdCfmMepMegId_Object((1,3,6,1,4,1,7483,6,4,1,1,3,1,9),_TnRmdCfmMepMegId_Type())
tnRmdCfmMepMegId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdCfmMepMegId.setStatus(_A)
_TnRmdCfmMepDirection_Type=Dot1agCfmMpDirection
_TnRmdCfmMepDirection_Object=MibTableColumn
tnRmdCfmMepDirection=_TnRmdCfmMepDirection_Object((1,3,6,1,4,1,7483,6,4,1,1,3,1,10),_TnRmdCfmMepDirection_Type())
tnRmdCfmMepDirection.setMaxAccess(_I)
if mibBuilder.loadTexts:tnRmdCfmMepDirection.setStatus(_A)
_TnRmdCfmMepLocalId_Type=Dot1agCfmMepId
_TnRmdCfmMepLocalId_Object=MibTableColumn
tnRmdCfmMepLocalId=_TnRmdCfmMepLocalId_Object((1,3,6,1,4,1,7483,6,4,1,1,3,1,11),_TnRmdCfmMepLocalId_Type())
tnRmdCfmMepLocalId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdCfmMepLocalId.setStatus(_A)
_TnRmdCfmMepEnabled_Type=TruthValue
_TnRmdCfmMepEnabled_Object=MibTableColumn
tnRmdCfmMepEnabled=_TnRmdCfmMepEnabled_Object((1,3,6,1,4,1,7483,6,4,1,1,3,1,12),_TnRmdCfmMepEnabled_Type())
tnRmdCfmMepEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdCfmMepEnabled.setStatus(_A)
_TnRmdCfmMepCcmEnabled_Type=TruthValue
_TnRmdCfmMepCcmEnabled_Object=MibTableColumn
tnRmdCfmMepCcmEnabled=_TnRmdCfmMepCcmEnabled_Object((1,3,6,1,4,1,7483,6,4,1,1,3,1,13),_TnRmdCfmMepCcmEnabled_Type())
tnRmdCfmMepCcmEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdCfmMepCcmEnabled.setStatus(_A)
_TnRmdCfmMepLbrEnabled_Type=TruthValue
_TnRmdCfmMepLbrEnabled_Object=MibTableColumn
tnRmdCfmMepLbrEnabled=_TnRmdCfmMepLbrEnabled_Object((1,3,6,1,4,1,7483,6,4,1,1,3,1,14),_TnRmdCfmMepLbrEnabled_Type())
tnRmdCfmMepLbrEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdCfmMepLbrEnabled.setStatus(_A)
_TnRmdCfmMepCcmInterval_Type=Dot1agCfmCcmInterval
_TnRmdCfmMepCcmInterval_Object=MibTableColumn
tnRmdCfmMepCcmInterval=_TnRmdCfmMepCcmInterval_Object((1,3,6,1,4,1,7483,6,4,1,1,3,1,15),_TnRmdCfmMepCcmInterval_Type())
tnRmdCfmMepCcmInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdCfmMepCcmInterval.setStatus(_A)
_TnRmdCfmMepIfIndex_Type=InterfaceIndexOrZero
_TnRmdCfmMepIfIndex_Object=MibTableColumn
tnRmdCfmMepIfIndex=_TnRmdCfmMepIfIndex_Object((1,3,6,1,4,1,7483,6,4,1,1,3,1,16),_TnRmdCfmMepIfIndex_Type())
tnRmdCfmMepIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdCfmMepIfIndex.setStatus(_A)
_TnRmdCfmMepVlanId_Type=VlanIdOrNone
_TnRmdCfmMepVlanId_Object=MibTableColumn
tnRmdCfmMepVlanId=_TnRmdCfmMepVlanId_Object((1,3,6,1,4,1,7483,6,4,1,1,3,1,17),_TnRmdCfmMepVlanId_Type())
tnRmdCfmMepVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdCfmMepVlanId.setStatus(_A)
_TnRmdCfmMepDefect_Type=TnRmdCfmMepDefect
_TnRmdCfmMepDefect_Object=MibTableColumn
tnRmdCfmMepDefect=_TnRmdCfmMepDefect_Object((1,3,6,1,4,1,7483,6,4,1,1,3,1,18),_TnRmdCfmMepDefect_Type())
tnRmdCfmMepDefect.setMaxAccess(_I)
if mibBuilder.loadTexts:tnRmdCfmMepDefect.setStatus(_A)
_TnRmdCfmMepRowStatus_Type=RowStatus
_TnRmdCfmMepRowStatus_Object=MibTableColumn
tnRmdCfmMepRowStatus=_TnRmdCfmMepRowStatus_Object((1,3,6,1,4,1,7483,6,4,1,1,3,1,19),_TnRmdCfmMepRowStatus_Type())
tnRmdCfmMepRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdCfmMepRowStatus.setStatus(_A)
class _TnRmdCfmMepEvcLoopbackEnabled_Type(TruthValue):defaultValue=2
_TnRmdCfmMepEvcLoopbackEnabled_Type.__name__=_N
_TnRmdCfmMepEvcLoopbackEnabled_Object=MibTableColumn
tnRmdCfmMepEvcLoopbackEnabled=_TnRmdCfmMepEvcLoopbackEnabled_Object((1,3,6,1,4,1,7483,6,4,1,1,3,1,20),_TnRmdCfmMepEvcLoopbackEnabled_Type())
tnRmdCfmMepEvcLoopbackEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdCfmMepEvcLoopbackEnabled.setStatus(_A)
_TnRmdCfmRemoteMepTable_Object=MibTable
tnRmdCfmRemoteMepTable=_TnRmdCfmRemoteMepTable_Object((1,3,6,1,4,1,7483,6,4,1,1,4))
if mibBuilder.loadTexts:tnRmdCfmRemoteMepTable.setStatus(_A)
_TnRmdCfmRemoteMepEntry_Object=MibTableRow
tnRmdCfmRemoteMepEntry=_TnRmdCfmRemoteMepEntry_Object((1,3,6,1,4,1,7483,6,4,1,1,4,1))
tnRmdCfmRemoteMepEntry.setIndexNames((0,_F,_G),(0,_D,_E),(0,_C,_H),(0,_C,_O))
if mibBuilder.loadTexts:tnRmdCfmRemoteMepEntry.setStatus(_A)
_TnRmdCfmRemoteMepId_Type=Dot1agCfmMepId
_TnRmdCfmRemoteMepId_Object=MibTableColumn
tnRmdCfmRemoteMepId=_TnRmdCfmRemoteMepId_Object((1,3,6,1,4,1,7483,6,4,1,1,4,1,1),_TnRmdCfmRemoteMepId_Type())
tnRmdCfmRemoteMepId.setMaxAccess(_K)
if mibBuilder.loadTexts:tnRmdCfmRemoteMepId.setStatus(_A)
_TnRmdCfmRemoteMepRowStatus_Type=RowStatus
_TnRmdCfmRemoteMepRowStatus_Object=MibTableColumn
tnRmdCfmRemoteMepRowStatus=_TnRmdCfmRemoteMepRowStatus_Object((1,3,6,1,4,1,7483,6,4,1,1,4,1,2),_TnRmdCfmRemoteMepRowStatus_Type())
tnRmdCfmRemoteMepRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdCfmRemoteMepRowStatus.setStatus(_A)
_TnRmdCfmMepDmTable_Object=MibTable
tnRmdCfmMepDmTable=_TnRmdCfmMepDmTable_Object((1,3,6,1,4,1,7483,6,4,1,1,5))
if mibBuilder.loadTexts:tnRmdCfmMepDmTable.setStatus(_A)
_TnRmdCfmMepDmEntry_Object=MibTableRow
tnRmdCfmMepDmEntry=_TnRmdCfmMepDmEntry_Object((1,3,6,1,4,1,7483,6,4,1,1,5,1))
tnRmdCfmMepDmEntry.setIndexNames((0,_F,_G),(0,_D,_E),(0,_C,_H))
if mibBuilder.loadTexts:tnRmdCfmMepDmEntry.setStatus(_A)
_TnRmdCfmMepDmResponder_Type=TruthValue
_TnRmdCfmMepDmResponder_Object=MibTableColumn
tnRmdCfmMepDmResponder=_TnRmdCfmMepDmResponder_Object((1,3,6,1,4,1,7483,6,4,1,1,5,1,1),_TnRmdCfmMepDmResponder_Type())
tnRmdCfmMepDmResponder.setMaxAccess(_J)
if mibBuilder.loadTexts:tnRmdCfmMepDmResponder.setStatus(_A)
_TnRmdCfmMepDmInitiatorSessionTable_Object=MibTable
tnRmdCfmMepDmInitiatorSessionTable=_TnRmdCfmMepDmInitiatorSessionTable_Object((1,3,6,1,4,1,7483,6,4,1,1,6))
if mibBuilder.loadTexts:tnRmdCfmMepDmInitiatorSessionTable.setStatus(_A)
_TnRmdCfmMepDmInitiatorSessionEntry_Object=MibTableRow
tnRmdCfmMepDmInitiatorSessionEntry=_TnRmdCfmMepDmInitiatorSessionEntry_Object((1,3,6,1,4,1,7483,6,4,1,1,6,1))
tnRmdCfmMepDmInitiatorSessionEntry.setIndexNames((0,_F,_G),(0,_D,_E),(0,_C,_H),(0,_C,_P))
if mibBuilder.loadTexts:tnRmdCfmMepDmInitiatorSessionEntry.setStatus(_A)
_TnRmdCfmMepDmInitiatorSessionNumber_Type=Unsigned32
_TnRmdCfmMepDmInitiatorSessionNumber_Object=MibTableColumn
tnRmdCfmMepDmInitiatorSessionNumber=_TnRmdCfmMepDmInitiatorSessionNumber_Object((1,3,6,1,4,1,7483,6,4,1,1,6,1,1),_TnRmdCfmMepDmInitiatorSessionNumber_Type())
tnRmdCfmMepDmInitiatorSessionNumber.setMaxAccess(_K)
if mibBuilder.loadTexts:tnRmdCfmMepDmInitiatorSessionNumber.setStatus(_A)
_TnRmdCfmMepDmInitiatorSessionType_Type=TnRmdCfmInitiatorSessionType
_TnRmdCfmMepDmInitiatorSessionType_Object=MibTableColumn
tnRmdCfmMepDmInitiatorSessionType=_TnRmdCfmMepDmInitiatorSessionType_Object((1,3,6,1,4,1,7483,6,4,1,1,6,1,2),_TnRmdCfmMepDmInitiatorSessionType_Type())
tnRmdCfmMepDmInitiatorSessionType.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdCfmMepDmInitiatorSessionType.setStatus(_A)
_TnRmdCfmMepDmInitiatorSessionMode_Type=TnRmdCfmDmInitiatorSessionMode
_TnRmdCfmMepDmInitiatorSessionMode_Object=MibTableColumn
tnRmdCfmMepDmInitiatorSessionMode=_TnRmdCfmMepDmInitiatorSessionMode_Object((1,3,6,1,4,1,7483,6,4,1,1,6,1,3),_TnRmdCfmMepDmInitiatorSessionMode_Type())
tnRmdCfmMepDmInitiatorSessionMode.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdCfmMepDmInitiatorSessionMode.setStatus(_A)
_TnRmdCfmMepDmInitiatorSessionInterval_Type=TnRmdCfmMeasurementInterval
_TnRmdCfmMepDmInitiatorSessionInterval_Object=MibTableColumn
tnRmdCfmMepDmInitiatorSessionInterval=_TnRmdCfmMepDmInitiatorSessionInterval_Object((1,3,6,1,4,1,7483,6,4,1,1,6,1,4),_TnRmdCfmMepDmInitiatorSessionInterval_Type())
tnRmdCfmMepDmInitiatorSessionInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdCfmMepDmInitiatorSessionInterval.setStatus(_A)
_TnRmdCfmMepDmInitiatorSessionTestInterval_Type=TnRmdCfmDmTestMeasurementInterval
_TnRmdCfmMepDmInitiatorSessionTestInterval_Object=MibTableColumn
tnRmdCfmMepDmInitiatorSessionTestInterval=_TnRmdCfmMepDmInitiatorSessionTestInterval_Object((1,3,6,1,4,1,7483,6,4,1,1,6,1,5),_TnRmdCfmMepDmInitiatorSessionTestInterval_Type())
tnRmdCfmMepDmInitiatorSessionTestInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdCfmMepDmInitiatorSessionTestInterval.setStatus(_A)
_TnRmdCfmMepDmInitiatorSessionPriority_Type=IEEE8021PriorityValue
_TnRmdCfmMepDmInitiatorSessionPriority_Object=MibTableColumn
tnRmdCfmMepDmInitiatorSessionPriority=_TnRmdCfmMepDmInitiatorSessionPriority_Object((1,3,6,1,4,1,7483,6,4,1,1,6,1,6),_TnRmdCfmMepDmInitiatorSessionPriority_Type())
tnRmdCfmMepDmInitiatorSessionPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdCfmMepDmInitiatorSessionPriority.setStatus(_A)
_TnRmdCfmMepDmInitiatorSessionDropEligible_Type=TruthValue
_TnRmdCfmMepDmInitiatorSessionDropEligible_Object=MibTableColumn
tnRmdCfmMepDmInitiatorSessionDropEligible=_TnRmdCfmMepDmInitiatorSessionDropEligible_Object((1,3,6,1,4,1,7483,6,4,1,1,6,1,7),_TnRmdCfmMepDmInitiatorSessionDropEligible_Type())
tnRmdCfmMepDmInitiatorSessionDropEligible.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdCfmMepDmInitiatorSessionDropEligible.setStatus(_A)
_TnRmdCfmMepDmInitiatorSessionDestMac_Type=MacAddress
_TnRmdCfmMepDmInitiatorSessionDestMac_Object=MibTableColumn
tnRmdCfmMepDmInitiatorSessionDestMac=_TnRmdCfmMepDmInitiatorSessionDestMac_Object((1,3,6,1,4,1,7483,6,4,1,1,6,1,8),_TnRmdCfmMepDmInitiatorSessionDestMac_Type())
tnRmdCfmMepDmInitiatorSessionDestMac.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdCfmMepDmInitiatorSessionDestMac.setStatus(_A)
_TnRmdCfmMepDmInitiatorSessionInsertTestIdTlv_Type=TruthValue
_TnRmdCfmMepDmInitiatorSessionInsertTestIdTlv_Object=MibTableColumn
tnRmdCfmMepDmInitiatorSessionInsertTestIdTlv=_TnRmdCfmMepDmInitiatorSessionInsertTestIdTlv_Object((1,3,6,1,4,1,7483,6,4,1,1,6,1,9),_TnRmdCfmMepDmInitiatorSessionInsertTestIdTlv_Type())
tnRmdCfmMepDmInitiatorSessionInsertTestIdTlv.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdCfmMepDmInitiatorSessionInsertTestIdTlv.setStatus(_A)
_TnRmdCfmMepDmInitiatorSessionTestId_Type=Unsigned32
_TnRmdCfmMepDmInitiatorSessionTestId_Object=MibTableColumn
tnRmdCfmMepDmInitiatorSessionTestId=_TnRmdCfmMepDmInitiatorSessionTestId_Object((1,3,6,1,4,1,7483,6,4,1,1,6,1,10),_TnRmdCfmMepDmInitiatorSessionTestId_Type())
tnRmdCfmMepDmInitiatorSessionTestId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdCfmMepDmInitiatorSessionTestId.setStatus(_A)
_TnRmdCfmMepDmInitiatorSessionFrameLength_Type=Unsigned32
_TnRmdCfmMepDmInitiatorSessionFrameLength_Object=MibTableColumn
tnRmdCfmMepDmInitiatorSessionFrameLength=_TnRmdCfmMepDmInitiatorSessionFrameLength_Object((1,3,6,1,4,1,7483,6,4,1,1,6,1,11),_TnRmdCfmMepDmInitiatorSessionFrameLength_Type())
tnRmdCfmMepDmInitiatorSessionFrameLength.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdCfmMepDmInitiatorSessionFrameLength.setStatus(_A)
_TnRmdCfmMepDmInitiatorSessionState_Type=TnRmdCfmInitiatorSessionState
_TnRmdCfmMepDmInitiatorSessionState_Object=MibTableColumn
tnRmdCfmMepDmInitiatorSessionState=_TnRmdCfmMepDmInitiatorSessionState_Object((1,3,6,1,4,1,7483,6,4,1,1,6,1,12),_TnRmdCfmMepDmInitiatorSessionState_Type())
tnRmdCfmMepDmInitiatorSessionState.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdCfmMepDmInitiatorSessionState.setStatus(_A)
_TnRmdCfmMepDmInitiatorSessionRowStatus_Type=RowStatus
_TnRmdCfmMepDmInitiatorSessionRowStatus_Object=MibTableColumn
tnRmdCfmMepDmInitiatorSessionRowStatus=_TnRmdCfmMepDmInitiatorSessionRowStatus_Object((1,3,6,1,4,1,7483,6,4,1,1,6,1,13),_TnRmdCfmMepDmInitiatorSessionRowStatus_Type())
tnRmdCfmMepDmInitiatorSessionRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdCfmMepDmInitiatorSessionRowStatus.setStatus(_A)
_TnRmdCfmMepSlmTable_Object=MibTable
tnRmdCfmMepSlmTable=_TnRmdCfmMepSlmTable_Object((1,3,6,1,4,1,7483,6,4,1,1,11))
if mibBuilder.loadTexts:tnRmdCfmMepSlmTable.setStatus(_A)
_TnRmdCfmMepSlmEntry_Object=MibTableRow
tnRmdCfmMepSlmEntry=_TnRmdCfmMepSlmEntry_Object((1,3,6,1,4,1,7483,6,4,1,1,11,1))
tnRmdCfmMepSlmEntry.setIndexNames((0,_F,_G),(0,_D,_E),(0,_C,_H))
if mibBuilder.loadTexts:tnRmdCfmMepSlmEntry.setStatus(_A)
_TnRmdCfmMepSlmResponder_Type=TruthValue
_TnRmdCfmMepSlmResponder_Object=MibTableColumn
tnRmdCfmMepSlmResponder=_TnRmdCfmMepSlmResponder_Object((1,3,6,1,4,1,7483,6,4,1,1,11,1,1),_TnRmdCfmMepSlmResponder_Type())
tnRmdCfmMepSlmResponder.setMaxAccess(_J)
if mibBuilder.loadTexts:tnRmdCfmMepSlmResponder.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'TnRmdCfmDmInitiatorSessionMode':TnRmdCfmDmInitiatorSessionMode,'TnRmdCfmDmTestMeasurementInterval':TnRmdCfmDmTestMeasurementInterval,'TnRmdCfmInitiatorSessionState':TnRmdCfmInitiatorSessionState,'TnRmdCfmInitiatorSessionType':TnRmdCfmInitiatorSessionType,'TnRmdCfmMegId':TnRmdCfmMegId,'TnRmdCfmMepDefect':TnRmdCfmMepDefect,'TnRmdCfmMepNumber':TnRmdCfmMepNumber,'TnRmdCfmMeasurementInterval':TnRmdCfmMeasurementInterval,'IEEE8021PriorityValue':IEEE8021PriorityValue,'tnRmdCfmMibModule':tnRmdCfmMibModule,'tnRmdCfmObjects':tnRmdCfmObjects,'tnRmdCfmAttributeTotal':tnRmdCfmAttributeTotal,'tnRmdSystemCfmTable':tnRmdSystemCfmTable,'tnRmdSystemCfmEntry':tnRmdSystemCfmEntry,'tnRmdSystemCfmMaxNrMeps':tnRmdSystemCfmMaxNrMeps,'tnRmdSystemCfmLmMaxNrPriorityLevels':tnRmdSystemCfmLmMaxNrPriorityLevels,'tnRmdSystemCfmDmUpdateLocalTime':tnRmdSystemCfmDmUpdateLocalTime,'tnRmdCfmMepTable':tnRmdCfmMepTable,'tnRmdCfmMepEntry':tnRmdCfmMepEntry,_H:tnRmdCfmMepNumber,'tnRmdCfmMepMdIndex':tnRmdCfmMepMdIndex,'tnRmdCfmMepMdFormat':tnRmdCfmMepMdFormat,'tnRmdCfmMepMdName':tnRmdCfmMepMdName,'tnRmdCfmMepMaIndex':tnRmdCfmMepMaIndex,'tnRmdCfmMepMaNetFormat':tnRmdCfmMepMaNetFormat,'tnRmdCfmMepMaNetName':tnRmdCfmMepMaNetName,'tnRmdCfmMepMdLevel':tnRmdCfmMepMdLevel,'tnRmdCfmMepMegId':tnRmdCfmMepMegId,'tnRmdCfmMepDirection':tnRmdCfmMepDirection,'tnRmdCfmMepLocalId':tnRmdCfmMepLocalId,'tnRmdCfmMepEnabled':tnRmdCfmMepEnabled,'tnRmdCfmMepCcmEnabled':tnRmdCfmMepCcmEnabled,'tnRmdCfmMepLbrEnabled':tnRmdCfmMepLbrEnabled,'tnRmdCfmMepCcmInterval':tnRmdCfmMepCcmInterval,'tnRmdCfmMepIfIndex':tnRmdCfmMepIfIndex,'tnRmdCfmMepVlanId':tnRmdCfmMepVlanId,'tnRmdCfmMepDefect':tnRmdCfmMepDefect,'tnRmdCfmMepRowStatus':tnRmdCfmMepRowStatus,'tnRmdCfmMepEvcLoopbackEnabled':tnRmdCfmMepEvcLoopbackEnabled,'tnRmdCfmRemoteMepTable':tnRmdCfmRemoteMepTable,'tnRmdCfmRemoteMepEntry':tnRmdCfmRemoteMepEntry,_O:tnRmdCfmRemoteMepId,'tnRmdCfmRemoteMepRowStatus':tnRmdCfmRemoteMepRowStatus,'tnRmdCfmMepDmTable':tnRmdCfmMepDmTable,'tnRmdCfmMepDmEntry':tnRmdCfmMepDmEntry,'tnRmdCfmMepDmResponder':tnRmdCfmMepDmResponder,'tnRmdCfmMepDmInitiatorSessionTable':tnRmdCfmMepDmInitiatorSessionTable,'tnRmdCfmMepDmInitiatorSessionEntry':tnRmdCfmMepDmInitiatorSessionEntry,_P:tnRmdCfmMepDmInitiatorSessionNumber,'tnRmdCfmMepDmInitiatorSessionType':tnRmdCfmMepDmInitiatorSessionType,'tnRmdCfmMepDmInitiatorSessionMode':tnRmdCfmMepDmInitiatorSessionMode,'tnRmdCfmMepDmInitiatorSessionInterval':tnRmdCfmMepDmInitiatorSessionInterval,'tnRmdCfmMepDmInitiatorSessionTestInterval':tnRmdCfmMepDmInitiatorSessionTestInterval,'tnRmdCfmMepDmInitiatorSessionPriority':tnRmdCfmMepDmInitiatorSessionPriority,'tnRmdCfmMepDmInitiatorSessionDropEligible':tnRmdCfmMepDmInitiatorSessionDropEligible,'tnRmdCfmMepDmInitiatorSessionDestMac':tnRmdCfmMepDmInitiatorSessionDestMac,'tnRmdCfmMepDmInitiatorSessionInsertTestIdTlv':tnRmdCfmMepDmInitiatorSessionInsertTestIdTlv,'tnRmdCfmMepDmInitiatorSessionTestId':tnRmdCfmMepDmInitiatorSessionTestId,'tnRmdCfmMepDmInitiatorSessionFrameLength':tnRmdCfmMepDmInitiatorSessionFrameLength,'tnRmdCfmMepDmInitiatorSessionState':tnRmdCfmMepDmInitiatorSessionState,'tnRmdCfmMepDmInitiatorSessionRowStatus':tnRmdCfmMepDmInitiatorSessionRowStatus,'tnRmdCfmMepSlmTable':tnRmdCfmMepSlmTable,'tnRmdCfmMepSlmEntry':tnRmdCfmMepSlmEntry,'tnRmdCfmMepSlmResponder':tnRmdCfmMepSlmResponder})