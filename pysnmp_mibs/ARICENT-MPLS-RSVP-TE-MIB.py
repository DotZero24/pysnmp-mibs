_Y='fsMplsRsvpTeIfStatsEntry'
_X='recoveryPathSRefresh'
_W='recoveryPathReceive'
_V='recoveryPathTransmit'
_U='fsMplsRsvpTeNbrIfAddr'
_T='notSupported'
_S='not-accessible'
_R='disable'
_Q='enable'
_P='AtmVcIdentifier'
_O='AtmVpIdentifier'
_N='fsMplsRsvpTeIfIndex'
_M='TimeInterval'
_L='StorageType'
_K='Bits'
_J='ARICENT-MPLS-RSVP-TE-MIB'
_I='disabled'
_H='enabled'
_G='TruthValue'
_F='Unsigned32'
_E='read-create'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI',_K,'Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'enterprises','iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_L,'TextualConvention',_M,'TimeStamp',_G)
fsMplsRsvpTeMIB=ModuleIdentity((1,3,6,1,4,1,2076,13,2))
if mibBuilder.loadTexts:fsMplsRsvpTeMIB.setRevisions(('2012-09-05 00:00',))
class MplsLsrIdentifier(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
class AtmVpIdentifier(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
class AtmVcIdentifier(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsMplsRsvpTeObjects_ObjectIdentity=ObjectIdentity
fsMplsRsvpTeObjects=_FsMplsRsvpTeObjects_ObjectIdentity((1,3,6,1,4,1,2076,13,2,1))
_FsMplsRsvpTeIfTable_Object=MibTable
fsMplsRsvpTeIfTable=_FsMplsRsvpTeIfTable_Object((1,3,6,1,4,1,2076,13,2,1,1))
if mibBuilder.loadTexts:fsMplsRsvpTeIfTable.setStatus(_A)
_FsMplsRsvpTeIfEntry_Object=MibTableRow
fsMplsRsvpTeIfEntry=_FsMplsRsvpTeIfEntry_Object((1,3,6,1,4,1,2076,13,2,1,1,1))
fsMplsRsvpTeIfEntry.setIndexNames((0,_J,_N))
if mibBuilder.loadTexts:fsMplsRsvpTeIfEntry.setStatus(_A)
_FsMplsRsvpTeIfIndex_Type=InterfaceIndex
_FsMplsRsvpTeIfIndex_Object=MibTableColumn
fsMplsRsvpTeIfIndex=_FsMplsRsvpTeIfIndex_Object((1,3,6,1,4,1,2076,13,2,1,1,1,1),_FsMplsRsvpTeIfIndex_Type())
fsMplsRsvpTeIfIndex.setMaxAccess(_S)
if mibBuilder.loadTexts:fsMplsRsvpTeIfIndex.setStatus(_A)
class _FsMplsRsvpTeIfLblSpace_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('perPlatform',1),('perInterface',2)))
_FsMplsRsvpTeIfLblSpace_Type.__name__=_D
_FsMplsRsvpTeIfLblSpace_Object=MibTableColumn
fsMplsRsvpTeIfLblSpace=_FsMplsRsvpTeIfLblSpace_Object((1,3,6,1,4,1,2076,13,2,1,1,1,2),_FsMplsRsvpTeIfLblSpace_Type())
fsMplsRsvpTeIfLblSpace.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMplsRsvpTeIfLblSpace.setStatus(_A)
class _FsMplsRsvpTeIfLblType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('rsvpTeIfEth',1),('rsvpTeIfAtm',2),('rsvpTeIfFr',3)))
_FsMplsRsvpTeIfLblType_Type.__name__=_D
_FsMplsRsvpTeIfLblType_Object=MibTableColumn
fsMplsRsvpTeIfLblType=_FsMplsRsvpTeIfLblType_Object((1,3,6,1,4,1,2076,13,2,1,1,1,3),_FsMplsRsvpTeIfLblType_Type())
fsMplsRsvpTeIfLblType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMplsRsvpTeIfLblType.setStatus(_A)
class _FsMplsRsvpTeAtmMergeCap_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2)));namedValues=NamedValues(*((_T,0),('vcMerge',2)))
_FsMplsRsvpTeAtmMergeCap_Type.__name__=_D
_FsMplsRsvpTeAtmMergeCap_Object=MibTableColumn
fsMplsRsvpTeAtmMergeCap=_FsMplsRsvpTeAtmMergeCap_Object((1,3,6,1,4,1,2076,13,2,1,1,1,4),_FsMplsRsvpTeAtmMergeCap_Type())
fsMplsRsvpTeAtmMergeCap.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMplsRsvpTeAtmMergeCap.setStatus(_A)
class _FsMplsRsvpTeAtmVcDirection_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('biDirectional',0),('oddUniDirectional',1),('evenUniDirectional',2)))
_FsMplsRsvpTeAtmVcDirection_Type.__name__=_D
_FsMplsRsvpTeAtmVcDirection_Object=MibTableColumn
fsMplsRsvpTeAtmVcDirection=_FsMplsRsvpTeAtmVcDirection_Object((1,3,6,1,4,1,2076,13,2,1,1,1,5),_FsMplsRsvpTeAtmVcDirection_Type())
fsMplsRsvpTeAtmVcDirection.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMplsRsvpTeAtmVcDirection.setStatus(_A)
class _FsMplsRsvpTeAtmMinVpi_Type(AtmVpIdentifier):defaultValue=0
_FsMplsRsvpTeAtmMinVpi_Type.__name__=_O
_FsMplsRsvpTeAtmMinVpi_Object=MibTableColumn
fsMplsRsvpTeAtmMinVpi=_FsMplsRsvpTeAtmMinVpi_Object((1,3,6,1,4,1,2076,13,2,1,1,1,6),_FsMplsRsvpTeAtmMinVpi_Type())
fsMplsRsvpTeAtmMinVpi.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMplsRsvpTeAtmMinVpi.setStatus(_A)
class _FsMplsRsvpTeAtmMinVci_Type(AtmVcIdentifier):defaultValue=33
_FsMplsRsvpTeAtmMinVci_Type.__name__=_P
_FsMplsRsvpTeAtmMinVci_Object=MibTableColumn
fsMplsRsvpTeAtmMinVci=_FsMplsRsvpTeAtmMinVci_Object((1,3,6,1,4,1,2076,13,2,1,1,1,7),_FsMplsRsvpTeAtmMinVci_Type())
fsMplsRsvpTeAtmMinVci.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMplsRsvpTeAtmMinVci.setStatus(_A)
class _FsMplsRsvpTeAtmMaxVpi_Type(AtmVpIdentifier):defaultValue=0
_FsMplsRsvpTeAtmMaxVpi_Type.__name__=_O
_FsMplsRsvpTeAtmMaxVpi_Object=MibTableColumn
fsMplsRsvpTeAtmMaxVpi=_FsMplsRsvpTeAtmMaxVpi_Object((1,3,6,1,4,1,2076,13,2,1,1,1,8),_FsMplsRsvpTeAtmMaxVpi_Type())
fsMplsRsvpTeAtmMaxVpi.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMplsRsvpTeAtmMaxVpi.setStatus(_A)
class _FsMplsRsvpTeAtmMaxVci_Type(AtmVcIdentifier):defaultValue=160
_FsMplsRsvpTeAtmMaxVci_Type.__name__=_P
_FsMplsRsvpTeAtmMaxVci_Object=MibTableColumn
fsMplsRsvpTeAtmMaxVci=_FsMplsRsvpTeAtmMaxVci_Object((1,3,6,1,4,1,2076,13,2,1,1,1,9),_FsMplsRsvpTeAtmMaxVci_Type())
fsMplsRsvpTeAtmMaxVci.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMplsRsvpTeAtmMaxVci.setStatus(_A)
class _FsMplsRsvpTeIfMtu_Type(Integer32):defaultValue=1500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1500,4096))
_FsMplsRsvpTeIfMtu_Type.__name__=_D
_FsMplsRsvpTeIfMtu_Object=MibTableColumn
fsMplsRsvpTeIfMtu=_FsMplsRsvpTeIfMtu_Object((1,3,6,1,4,1,2076,13,2,1,1,1,10),_FsMplsRsvpTeIfMtu_Type())
fsMplsRsvpTeIfMtu.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMplsRsvpTeIfMtu.setStatus(_A)
_FsMplsRsvpTeIfUdpNbrs_Type=Counter32
_FsMplsRsvpTeIfUdpNbrs_Object=MibTableColumn
fsMplsRsvpTeIfUdpNbrs=_FsMplsRsvpTeIfUdpNbrs_Object((1,3,6,1,4,1,2076,13,2,1,1,1,11),_FsMplsRsvpTeIfUdpNbrs_Type())
fsMplsRsvpTeIfUdpNbrs.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsRsvpTeIfUdpNbrs.setStatus(_A)
_FsMplsRsvpTeIfIpNbrs_Type=Counter32
_FsMplsRsvpTeIfIpNbrs_Object=MibTableColumn
fsMplsRsvpTeIfIpNbrs=_FsMplsRsvpTeIfIpNbrs_Object((1,3,6,1,4,1,2076,13,2,1,1,1,12),_FsMplsRsvpTeIfIpNbrs_Type())
fsMplsRsvpTeIfIpNbrs.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsRsvpTeIfIpNbrs.setStatus(_A)
_FsMplsRsvpTeIfNbrs_Type=Counter32
_FsMplsRsvpTeIfNbrs_Object=MibTableColumn
fsMplsRsvpTeIfNbrs=_FsMplsRsvpTeIfNbrs_Object((1,3,6,1,4,1,2076,13,2,1,1,1,13),_FsMplsRsvpTeIfNbrs_Type())
fsMplsRsvpTeIfNbrs.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsRsvpTeIfNbrs.setStatus(_A)
class _FsMplsRsvpTeIfRefreshMultiple_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_FsMplsRsvpTeIfRefreshMultiple_Type.__name__=_D
_FsMplsRsvpTeIfRefreshMultiple_Object=MibTableColumn
fsMplsRsvpTeIfRefreshMultiple=_FsMplsRsvpTeIfRefreshMultiple_Object((1,3,6,1,4,1,2076,13,2,1,1,1,14),_FsMplsRsvpTeIfRefreshMultiple_Type())
fsMplsRsvpTeIfRefreshMultiple.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMplsRsvpTeIfRefreshMultiple.setStatus(_A)
class _FsMplsRsvpTeIfTTL_Type(Integer32):defaultValue=64
_FsMplsRsvpTeIfTTL_Type.__name__=_D
_FsMplsRsvpTeIfTTL_Object=MibTableColumn
fsMplsRsvpTeIfTTL=_FsMplsRsvpTeIfTTL_Object((1,3,6,1,4,1,2076,13,2,1,1,1,15),_FsMplsRsvpTeIfTTL_Type())
fsMplsRsvpTeIfTTL.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMplsRsvpTeIfTTL.setStatus(_A)
class _FsMplsRsvpTeIfRefreshInterval_Type(TimeInterval):defaultValue=30000
_FsMplsRsvpTeIfRefreshInterval_Type.__name__=_M
_FsMplsRsvpTeIfRefreshInterval_Object=MibTableColumn
fsMplsRsvpTeIfRefreshInterval=_FsMplsRsvpTeIfRefreshInterval_Object((1,3,6,1,4,1,2076,13,2,1,1,1,16),_FsMplsRsvpTeIfRefreshInterval_Type())
fsMplsRsvpTeIfRefreshInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMplsRsvpTeIfRefreshInterval.setStatus(_A)
class _FsMplsRsvpTeIfRouteDelay_Type(TimeInterval):defaultValue=2
_FsMplsRsvpTeIfRouteDelay_Type.__name__=_M
_FsMplsRsvpTeIfRouteDelay_Object=MibTableColumn
fsMplsRsvpTeIfRouteDelay=_FsMplsRsvpTeIfRouteDelay_Object((1,3,6,1,4,1,2076,13,2,1,1,1,17),_FsMplsRsvpTeIfRouteDelay_Type())
fsMplsRsvpTeIfRouteDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMplsRsvpTeIfRouteDelay.setStatus(_A)
class _FsMplsRsvpTeIfUdpRequired_Type(TruthValue):defaultValue=2
_FsMplsRsvpTeIfUdpRequired_Type.__name__=_G
_FsMplsRsvpTeIfUdpRequired_Object=MibTableColumn
fsMplsRsvpTeIfUdpRequired=_FsMplsRsvpTeIfUdpRequired_Object((1,3,6,1,4,1,2076,13,2,1,1,1,18),_FsMplsRsvpTeIfUdpRequired_Type())
fsMplsRsvpTeIfUdpRequired.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMplsRsvpTeIfUdpRequired.setStatus(_A)
class _FsMplsRsvpTeIfHelloSupported_Type(TruthValue):defaultValue=2
_FsMplsRsvpTeIfHelloSupported_Type.__name__=_G
_FsMplsRsvpTeIfHelloSupported_Object=MibTableColumn
fsMplsRsvpTeIfHelloSupported=_FsMplsRsvpTeIfHelloSupported_Object((1,3,6,1,4,1,2076,13,2,1,1,1,19),_FsMplsRsvpTeIfHelloSupported_Type())
fsMplsRsvpTeIfHelloSupported.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMplsRsvpTeIfHelloSupported.setStatus(_A)
class _FsMplsRsvpTeIfLinkAttr_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_FsMplsRsvpTeIfLinkAttr_Type.__name__=_F
_FsMplsRsvpTeIfLinkAttr_Object=MibTableColumn
fsMplsRsvpTeIfLinkAttr=_FsMplsRsvpTeIfLinkAttr_Object((1,3,6,1,4,1,2076,13,2,1,1,1,20),_FsMplsRsvpTeIfLinkAttr_Type())
fsMplsRsvpTeIfLinkAttr.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMplsRsvpTeIfLinkAttr.setStatus(_A)
_FsMplsRsvpTeIfStatus_Type=RowStatus
_FsMplsRsvpTeIfStatus_Object=MibTableColumn
fsMplsRsvpTeIfStatus=_FsMplsRsvpTeIfStatus_Object((1,3,6,1,4,1,2076,13,2,1,1,1,21),_FsMplsRsvpTeIfStatus_Type())
fsMplsRsvpTeIfStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMplsRsvpTeIfStatus.setStatus(_A)
_FsMplsRsvpTeIfPlrId_Type=MplsLsrIdentifier
_FsMplsRsvpTeIfPlrId_Object=MibTableColumn
fsMplsRsvpTeIfPlrId=_FsMplsRsvpTeIfPlrId_Object((1,3,6,1,4,1,2076,13,2,1,1,1,22),_FsMplsRsvpTeIfPlrId_Type())
fsMplsRsvpTeIfPlrId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMplsRsvpTeIfPlrId.setStatus(_A)
_FsMplsRsvpTeIfAvoidNodeId_Type=MplsLsrIdentifier
_FsMplsRsvpTeIfAvoidNodeId_Object=MibTableColumn
fsMplsRsvpTeIfAvoidNodeId=_FsMplsRsvpTeIfAvoidNodeId_Object((1,3,6,1,4,1,2076,13,2,1,1,1,23),_FsMplsRsvpTeIfAvoidNodeId_Type())
fsMplsRsvpTeIfAvoidNodeId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMplsRsvpTeIfAvoidNodeId.setStatus(_A)
class _FsMplsRsvpTeIfStorageType_Type(StorageType):defaultValue=3
_FsMplsRsvpTeIfStorageType_Type.__name__=_L
_FsMplsRsvpTeIfStorageType_Object=MibTableColumn
fsMplsRsvpTeIfStorageType=_FsMplsRsvpTeIfStorageType_Object((1,3,6,1,4,1,2076,13,2,1,1,1,24),_FsMplsRsvpTeIfStorageType_Type())
fsMplsRsvpTeIfStorageType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMplsRsvpTeIfStorageType.setStatus(_A)
_FsMplsRsvpTeIfStatsTable_Object=MibTable
fsMplsRsvpTeIfStatsTable=_FsMplsRsvpTeIfStatsTable_Object((1,3,6,1,4,1,2076,13,2,1,2))
if mibBuilder.loadTexts:fsMplsRsvpTeIfStatsTable.setStatus(_A)
_FsMplsRsvpTeIfStatsEntry_Object=MibTableRow
fsMplsRsvpTeIfStatsEntry=_FsMplsRsvpTeIfStatsEntry_Object((1,3,6,1,4,1,2076,13,2,1,2,1))
if mibBuilder.loadTexts:fsMplsRsvpTeIfStatsEntry.setStatus(_A)
_FsMplsRsvpTeIfNumTnls_Type=Counter32
_FsMplsRsvpTeIfNumTnls_Object=MibTableColumn
fsMplsRsvpTeIfNumTnls=_FsMplsRsvpTeIfNumTnls_Object((1,3,6,1,4,1,2076,13,2,1,2,1,1),_FsMplsRsvpTeIfNumTnls_Type())
fsMplsRsvpTeIfNumTnls.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsRsvpTeIfNumTnls.setStatus(_A)
_FsMplsRsvpTeIfNumMsgSent_Type=Counter32
_FsMplsRsvpTeIfNumMsgSent_Object=MibTableColumn
fsMplsRsvpTeIfNumMsgSent=_FsMplsRsvpTeIfNumMsgSent_Object((1,3,6,1,4,1,2076,13,2,1,2,1,2),_FsMplsRsvpTeIfNumMsgSent_Type())
fsMplsRsvpTeIfNumMsgSent.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsRsvpTeIfNumMsgSent.setStatus(_A)
_FsMplsRsvpTeIfNumMsgRcvd_Type=Counter32
_FsMplsRsvpTeIfNumMsgRcvd_Object=MibTableColumn
fsMplsRsvpTeIfNumMsgRcvd=_FsMplsRsvpTeIfNumMsgRcvd_Object((1,3,6,1,4,1,2076,13,2,1,2,1,3),_FsMplsRsvpTeIfNumMsgRcvd_Type())
fsMplsRsvpTeIfNumMsgRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsRsvpTeIfNumMsgRcvd.setStatus(_A)
_FsMplsRsvpTeIfNumHelloSent_Type=Counter32
_FsMplsRsvpTeIfNumHelloSent_Object=MibTableColumn
fsMplsRsvpTeIfNumHelloSent=_FsMplsRsvpTeIfNumHelloSent_Object((1,3,6,1,4,1,2076,13,2,1,2,1,4),_FsMplsRsvpTeIfNumHelloSent_Type())
fsMplsRsvpTeIfNumHelloSent.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsRsvpTeIfNumHelloSent.setStatus(_A)
_FsMplsRsvpTeIfNumHelloRcvd_Type=Counter32
_FsMplsRsvpTeIfNumHelloRcvd_Object=MibTableColumn
fsMplsRsvpTeIfNumHelloRcvd=_FsMplsRsvpTeIfNumHelloRcvd_Object((1,3,6,1,4,1,2076,13,2,1,2,1,5),_FsMplsRsvpTeIfNumHelloRcvd_Type())
fsMplsRsvpTeIfNumHelloRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsRsvpTeIfNumHelloRcvd.setStatus(_A)
_FsMplsRsvpTeIfNumPathErrSent_Type=Counter32
_FsMplsRsvpTeIfNumPathErrSent_Object=MibTableColumn
fsMplsRsvpTeIfNumPathErrSent=_FsMplsRsvpTeIfNumPathErrSent_Object((1,3,6,1,4,1,2076,13,2,1,2,1,6),_FsMplsRsvpTeIfNumPathErrSent_Type())
fsMplsRsvpTeIfNumPathErrSent.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsRsvpTeIfNumPathErrSent.setStatus(_A)
_FsMplsRsvpTeIfNumPathErrRcvd_Type=Counter32
_FsMplsRsvpTeIfNumPathErrRcvd_Object=MibTableColumn
fsMplsRsvpTeIfNumPathErrRcvd=_FsMplsRsvpTeIfNumPathErrRcvd_Object((1,3,6,1,4,1,2076,13,2,1,2,1,7),_FsMplsRsvpTeIfNumPathErrRcvd_Type())
fsMplsRsvpTeIfNumPathErrRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsRsvpTeIfNumPathErrRcvd.setStatus(_A)
_FsMplsRsvpTeIfNumPathTearSent_Type=Counter32
_FsMplsRsvpTeIfNumPathTearSent_Object=MibTableColumn
fsMplsRsvpTeIfNumPathTearSent=_FsMplsRsvpTeIfNumPathTearSent_Object((1,3,6,1,4,1,2076,13,2,1,2,1,8),_FsMplsRsvpTeIfNumPathTearSent_Type())
fsMplsRsvpTeIfNumPathTearSent.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsRsvpTeIfNumPathTearSent.setStatus(_A)
_FsMplsRsvpTeIfNumPathTearRcvd_Type=Counter32
_FsMplsRsvpTeIfNumPathTearRcvd_Object=MibTableColumn
fsMplsRsvpTeIfNumPathTearRcvd=_FsMplsRsvpTeIfNumPathTearRcvd_Object((1,3,6,1,4,1,2076,13,2,1,2,1,9),_FsMplsRsvpTeIfNumPathTearRcvd_Type())
fsMplsRsvpTeIfNumPathTearRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsRsvpTeIfNumPathTearRcvd.setStatus(_A)
_FsMplsRsvpTeIfNumResvErrSent_Type=Counter32
_FsMplsRsvpTeIfNumResvErrSent_Object=MibTableColumn
fsMplsRsvpTeIfNumResvErrSent=_FsMplsRsvpTeIfNumResvErrSent_Object((1,3,6,1,4,1,2076,13,2,1,2,1,10),_FsMplsRsvpTeIfNumResvErrSent_Type())
fsMplsRsvpTeIfNumResvErrSent.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsRsvpTeIfNumResvErrSent.setStatus(_A)
_FsMplsRsvpTeIfNumResvErrRcvd_Type=Counter32
_FsMplsRsvpTeIfNumResvErrRcvd_Object=MibTableColumn
fsMplsRsvpTeIfNumResvErrRcvd=_FsMplsRsvpTeIfNumResvErrRcvd_Object((1,3,6,1,4,1,2076,13,2,1,2,1,11),_FsMplsRsvpTeIfNumResvErrRcvd_Type())
fsMplsRsvpTeIfNumResvErrRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsRsvpTeIfNumResvErrRcvd.setStatus(_A)
_FsMplsRsvpTeIfNumResvTearSent_Type=Counter32
_FsMplsRsvpTeIfNumResvTearSent_Object=MibTableColumn
fsMplsRsvpTeIfNumResvTearSent=_FsMplsRsvpTeIfNumResvTearSent_Object((1,3,6,1,4,1,2076,13,2,1,2,1,12),_FsMplsRsvpTeIfNumResvTearSent_Type())
fsMplsRsvpTeIfNumResvTearSent.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsRsvpTeIfNumResvTearSent.setStatus(_A)
_FsMplsRsvpTeIfNumResvTearRcvd_Type=Counter32
_FsMplsRsvpTeIfNumResvTearRcvd_Object=MibTableColumn
fsMplsRsvpTeIfNumResvTearRcvd=_FsMplsRsvpTeIfNumResvTearRcvd_Object((1,3,6,1,4,1,2076,13,2,1,2,1,13),_FsMplsRsvpTeIfNumResvTearRcvd_Type())
fsMplsRsvpTeIfNumResvTearRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsRsvpTeIfNumResvTearRcvd.setStatus(_A)
_FsMplsRsvpTeIfNumResvConfSent_Type=Counter32
_FsMplsRsvpTeIfNumResvConfSent_Object=MibTableColumn
fsMplsRsvpTeIfNumResvConfSent=_FsMplsRsvpTeIfNumResvConfSent_Object((1,3,6,1,4,1,2076,13,2,1,2,1,14),_FsMplsRsvpTeIfNumResvConfSent_Type())
fsMplsRsvpTeIfNumResvConfSent.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsRsvpTeIfNumResvConfSent.setStatus(_A)
_FsMplsRsvpTeIfNumResvConfRcvd_Type=Counter32
_FsMplsRsvpTeIfNumResvConfRcvd_Object=MibTableColumn
fsMplsRsvpTeIfNumResvConfRcvd=_FsMplsRsvpTeIfNumResvConfRcvd_Object((1,3,6,1,4,1,2076,13,2,1,2,1,15),_FsMplsRsvpTeIfNumResvConfRcvd_Type())
fsMplsRsvpTeIfNumResvConfRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsRsvpTeIfNumResvConfRcvd.setStatus(_A)
_FsMplsRsvpTeIfNumBundleMsgSent_Type=Counter32
_FsMplsRsvpTeIfNumBundleMsgSent_Object=MibTableColumn
fsMplsRsvpTeIfNumBundleMsgSent=_FsMplsRsvpTeIfNumBundleMsgSent_Object((1,3,6,1,4,1,2076,13,2,1,2,1,16),_FsMplsRsvpTeIfNumBundleMsgSent_Type())
fsMplsRsvpTeIfNumBundleMsgSent.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsRsvpTeIfNumBundleMsgSent.setStatus(_A)
_FsMplsRsvpTeIfNumBundleMsgRcvd_Type=Counter32
_FsMplsRsvpTeIfNumBundleMsgRcvd_Object=MibTableColumn
fsMplsRsvpTeIfNumBundleMsgRcvd=_FsMplsRsvpTeIfNumBundleMsgRcvd_Object((1,3,6,1,4,1,2076,13,2,1,2,1,17),_FsMplsRsvpTeIfNumBundleMsgRcvd_Type())
fsMplsRsvpTeIfNumBundleMsgRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsRsvpTeIfNumBundleMsgRcvd.setStatus(_A)
_FsMplsRsvpTeIfNumSRefreshMsgSent_Type=Counter32
_FsMplsRsvpTeIfNumSRefreshMsgSent_Object=MibTableColumn
fsMplsRsvpTeIfNumSRefreshMsgSent=_FsMplsRsvpTeIfNumSRefreshMsgSent_Object((1,3,6,1,4,1,2076,13,2,1,2,1,18),_FsMplsRsvpTeIfNumSRefreshMsgSent_Type())
fsMplsRsvpTeIfNumSRefreshMsgSent.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsRsvpTeIfNumSRefreshMsgSent.setStatus(_A)
_FsMplsRsvpTeIfNumSRefreshMsgRcvd_Type=Counter32
_FsMplsRsvpTeIfNumSRefreshMsgRcvd_Object=MibTableColumn
fsMplsRsvpTeIfNumSRefreshMsgRcvd=_FsMplsRsvpTeIfNumSRefreshMsgRcvd_Object((1,3,6,1,4,1,2076,13,2,1,2,1,19),_FsMplsRsvpTeIfNumSRefreshMsgRcvd_Type())
fsMplsRsvpTeIfNumSRefreshMsgRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsRsvpTeIfNumSRefreshMsgRcvd.setStatus(_A)
_FsMplsRsvpTeIfNumPathSent_Type=Counter32
_FsMplsRsvpTeIfNumPathSent_Object=MibTableColumn
fsMplsRsvpTeIfNumPathSent=_FsMplsRsvpTeIfNumPathSent_Object((1,3,6,1,4,1,2076,13,2,1,2,1,20),_FsMplsRsvpTeIfNumPathSent_Type())
fsMplsRsvpTeIfNumPathSent.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsRsvpTeIfNumPathSent.setStatus(_A)
_FsMplsRsvpTeIfNumPathRcvd_Type=Counter32
_FsMplsRsvpTeIfNumPathRcvd_Object=MibTableColumn
fsMplsRsvpTeIfNumPathRcvd=_FsMplsRsvpTeIfNumPathRcvd_Object((1,3,6,1,4,1,2076,13,2,1,2,1,21),_FsMplsRsvpTeIfNumPathRcvd_Type())
fsMplsRsvpTeIfNumPathRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsRsvpTeIfNumPathRcvd.setStatus(_A)
_FsMplsRsvpTeIfNumResvSent_Type=Counter32
_FsMplsRsvpTeIfNumResvSent_Object=MibTableColumn
fsMplsRsvpTeIfNumResvSent=_FsMplsRsvpTeIfNumResvSent_Object((1,3,6,1,4,1,2076,13,2,1,2,1,22),_FsMplsRsvpTeIfNumResvSent_Type())
fsMplsRsvpTeIfNumResvSent.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsRsvpTeIfNumResvSent.setStatus(_A)
_FsMplsRsvpTeIfNumResvRcvd_Type=Counter32
_FsMplsRsvpTeIfNumResvRcvd_Object=MibTableColumn
fsMplsRsvpTeIfNumResvRcvd=_FsMplsRsvpTeIfNumResvRcvd_Object((1,3,6,1,4,1,2076,13,2,1,2,1,23),_FsMplsRsvpTeIfNumResvRcvd_Type())
fsMplsRsvpTeIfNumResvRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsRsvpTeIfNumResvRcvd.setStatus(_A)
_FsMplsRsvpTeIfNumNotifyMsgSent_Type=Counter32
_FsMplsRsvpTeIfNumNotifyMsgSent_Object=MibTableColumn
fsMplsRsvpTeIfNumNotifyMsgSent=_FsMplsRsvpTeIfNumNotifyMsgSent_Object((1,3,6,1,4,1,2076,13,2,1,2,1,24),_FsMplsRsvpTeIfNumNotifyMsgSent_Type())
fsMplsRsvpTeIfNumNotifyMsgSent.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsRsvpTeIfNumNotifyMsgSent.setStatus(_A)
_FsMplsRsvpTeIfNumNotifyMsgRcvd_Type=Counter32
_FsMplsRsvpTeIfNumNotifyMsgRcvd_Object=MibTableColumn
fsMplsRsvpTeIfNumNotifyMsgRcvd=_FsMplsRsvpTeIfNumNotifyMsgRcvd_Object((1,3,6,1,4,1,2076,13,2,1,2,1,25),_FsMplsRsvpTeIfNumNotifyMsgRcvd_Type())
fsMplsRsvpTeIfNumNotifyMsgRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsRsvpTeIfNumNotifyMsgRcvd.setStatus(_A)
_FsMplsRsvpTeIfNumRecoveryPathSent_Type=Counter32
_FsMplsRsvpTeIfNumRecoveryPathSent_Object=MibTableColumn
fsMplsRsvpTeIfNumRecoveryPathSent=_FsMplsRsvpTeIfNumRecoveryPathSent_Object((1,3,6,1,4,1,2076,13,2,1,2,1,26),_FsMplsRsvpTeIfNumRecoveryPathSent_Type())
fsMplsRsvpTeIfNumRecoveryPathSent.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsRsvpTeIfNumRecoveryPathSent.setStatus(_A)
_FsMplsRsvpTeIfNumRecoveryPathRcvd_Type=Counter32
_FsMplsRsvpTeIfNumRecoveryPathRcvd_Object=MibTableColumn
fsMplsRsvpTeIfNumRecoveryPathRcvd=_FsMplsRsvpTeIfNumRecoveryPathRcvd_Object((1,3,6,1,4,1,2076,13,2,1,2,1,27),_FsMplsRsvpTeIfNumRecoveryPathRcvd_Type())
fsMplsRsvpTeIfNumRecoveryPathRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsRsvpTeIfNumRecoveryPathRcvd.setStatus(_A)
_FsMplsRsvpTeIfNumPathSentWithRecoveryLbl_Type=Counter32
_FsMplsRsvpTeIfNumPathSentWithRecoveryLbl_Object=MibTableColumn
fsMplsRsvpTeIfNumPathSentWithRecoveryLbl=_FsMplsRsvpTeIfNumPathSentWithRecoveryLbl_Object((1,3,6,1,4,1,2076,13,2,1,2,1,28),_FsMplsRsvpTeIfNumPathSentWithRecoveryLbl_Type())
fsMplsRsvpTeIfNumPathSentWithRecoveryLbl.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsRsvpTeIfNumPathSentWithRecoveryLbl.setStatus(_A)
_FsMplsRsvpTeIfNumPathRcvdWithRecoveryLbl_Type=Counter32
_FsMplsRsvpTeIfNumPathRcvdWithRecoveryLbl_Object=MibTableColumn
fsMplsRsvpTeIfNumPathRcvdWithRecoveryLbl=_FsMplsRsvpTeIfNumPathRcvdWithRecoveryLbl_Object((1,3,6,1,4,1,2076,13,2,1,2,1,29),_FsMplsRsvpTeIfNumPathRcvdWithRecoveryLbl_Type())
fsMplsRsvpTeIfNumPathRcvdWithRecoveryLbl.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsRsvpTeIfNumPathRcvdWithRecoveryLbl.setStatus(_A)
_FsMplsRsvpTeIfNumPathSentWithSuggestedLbl_Type=Counter32
_FsMplsRsvpTeIfNumPathSentWithSuggestedLbl_Object=MibTableColumn
fsMplsRsvpTeIfNumPathSentWithSuggestedLbl=_FsMplsRsvpTeIfNumPathSentWithSuggestedLbl_Object((1,3,6,1,4,1,2076,13,2,1,2,1,30),_FsMplsRsvpTeIfNumPathSentWithSuggestedLbl_Type())
fsMplsRsvpTeIfNumPathSentWithSuggestedLbl.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsRsvpTeIfNumPathSentWithSuggestedLbl.setStatus(_A)
_FsMplsRsvpTeIfNumPathRcvdWithSuggestedLbl_Type=Counter32
_FsMplsRsvpTeIfNumPathRcvdWithSuggestedLbl_Object=MibTableColumn
fsMplsRsvpTeIfNumPathRcvdWithSuggestedLbl=_FsMplsRsvpTeIfNumPathRcvdWithSuggestedLbl_Object((1,3,6,1,4,1,2076,13,2,1,2,1,31),_FsMplsRsvpTeIfNumPathRcvdWithSuggestedLbl_Type())
fsMplsRsvpTeIfNumPathRcvdWithSuggestedLbl.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsRsvpTeIfNumPathRcvdWithSuggestedLbl.setStatus(_A)
_FsMplsRsvpTeIfNumHelloSentWithRestartCap_Type=Counter32
_FsMplsRsvpTeIfNumHelloSentWithRestartCap_Object=MibTableColumn
fsMplsRsvpTeIfNumHelloSentWithRestartCap=_FsMplsRsvpTeIfNumHelloSentWithRestartCap_Object((1,3,6,1,4,1,2076,13,2,1,2,1,32),_FsMplsRsvpTeIfNumHelloSentWithRestartCap_Type())
fsMplsRsvpTeIfNumHelloSentWithRestartCap.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsRsvpTeIfNumHelloSentWithRestartCap.setStatus(_A)
_FsMplsRsvpTeIfNumHelloRcvdWithRestartCap_Type=Counter32
_FsMplsRsvpTeIfNumHelloRcvdWithRestartCap_Object=MibTableColumn
fsMplsRsvpTeIfNumHelloRcvdWithRestartCap=_FsMplsRsvpTeIfNumHelloRcvdWithRestartCap_Object((1,3,6,1,4,1,2076,13,2,1,2,1,33),_FsMplsRsvpTeIfNumHelloRcvdWithRestartCap_Type())
fsMplsRsvpTeIfNumHelloRcvdWithRestartCap.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsRsvpTeIfNumHelloRcvdWithRestartCap.setStatus(_A)
_FsMplsRsvpTeIfNumHelloSentWithCapability_Type=Counter32
_FsMplsRsvpTeIfNumHelloSentWithCapability_Object=MibTableColumn
fsMplsRsvpTeIfNumHelloSentWithCapability=_FsMplsRsvpTeIfNumHelloSentWithCapability_Object((1,3,6,1,4,1,2076,13,2,1,2,1,34),_FsMplsRsvpTeIfNumHelloSentWithCapability_Type())
fsMplsRsvpTeIfNumHelloSentWithCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsRsvpTeIfNumHelloSentWithCapability.setStatus(_A)
_FsMplsRsvpTeIfNumHelloRcvdWithCapability_Type=Counter32
_FsMplsRsvpTeIfNumHelloRcvdWithCapability_Object=MibTableColumn
fsMplsRsvpTeIfNumHelloRcvdWithCapability=_FsMplsRsvpTeIfNumHelloRcvdWithCapability_Object((1,3,6,1,4,1,2076,13,2,1,2,1,35),_FsMplsRsvpTeIfNumHelloRcvdWithCapability_Type())
fsMplsRsvpTeIfNumHelloRcvdWithCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsRsvpTeIfNumHelloRcvdWithCapability.setStatus(_A)
_FsMplsRsvpTeIfNumPktDiscrded_Type=Counter32
_FsMplsRsvpTeIfNumPktDiscrded_Object=MibTableColumn
fsMplsRsvpTeIfNumPktDiscrded=_FsMplsRsvpTeIfNumPktDiscrded_Object((1,3,6,1,4,1,2076,13,2,1,2,1,36),_FsMplsRsvpTeIfNumPktDiscrded_Type())
fsMplsRsvpTeIfNumPktDiscrded.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsRsvpTeIfNumPktDiscrded.setStatus(_A)
_FsMplsRsvpTeNbrTable_Object=MibTable
fsMplsRsvpTeNbrTable=_FsMplsRsvpTeNbrTable_Object((1,3,6,1,4,1,2076,13,2,1,3))
if mibBuilder.loadTexts:fsMplsRsvpTeNbrTable.setStatus(_A)
_FsMplsRsvpTeNbrEntry_Object=MibTableRow
fsMplsRsvpTeNbrEntry=_FsMplsRsvpTeNbrEntry_Object((1,3,6,1,4,1,2076,13,2,1,3,1))
fsMplsRsvpTeNbrEntry.setIndexNames((0,_J,_N),(0,_J,_U))
if mibBuilder.loadTexts:fsMplsRsvpTeNbrEntry.setStatus(_A)
_FsMplsRsvpTeNbrIfAddr_Type=IpAddress
_FsMplsRsvpTeNbrIfAddr_Object=MibTableColumn
fsMplsRsvpTeNbrIfAddr=_FsMplsRsvpTeNbrIfAddr_Object((1,3,6,1,4,1,2076,13,2,1,3,1,1),_FsMplsRsvpTeNbrIfAddr_Type())
fsMplsRsvpTeNbrIfAddr.setMaxAccess(_S)
if mibBuilder.loadTexts:fsMplsRsvpTeNbrIfAddr.setStatus(_A)
class _FsMplsRsvpTeNbrRRCapable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_FsMplsRsvpTeNbrRRCapable_Type.__name__=_D
_FsMplsRsvpTeNbrRRCapable_Object=MibTableColumn
fsMplsRsvpTeNbrRRCapable=_FsMplsRsvpTeNbrRRCapable_Object((1,3,6,1,4,1,2076,13,2,1,3,1,2),_FsMplsRsvpTeNbrRRCapable_Type())
fsMplsRsvpTeNbrRRCapable.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMplsRsvpTeNbrRRCapable.setStatus(_A)
class _FsMplsRsvpTeNbrRRState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_FsMplsRsvpTeNbrRRState_Type.__name__=_D
_FsMplsRsvpTeNbrRRState_Object=MibTableColumn
fsMplsRsvpTeNbrRRState=_FsMplsRsvpTeNbrRRState_Object((1,3,6,1,4,1,2076,13,2,1,3,1,3),_FsMplsRsvpTeNbrRRState_Type())
fsMplsRsvpTeNbrRRState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsRsvpTeNbrRRState.setStatus(_A)
class _FsMplsRsvpTeNbrRMDCapable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_FsMplsRsvpTeNbrRMDCapable_Type.__name__=_D
_FsMplsRsvpTeNbrRMDCapable_Object=MibTableColumn
fsMplsRsvpTeNbrRMDCapable=_FsMplsRsvpTeNbrRMDCapable_Object((1,3,6,1,4,1,2076,13,2,1,3,1,4),_FsMplsRsvpTeNbrRMDCapable_Type())
fsMplsRsvpTeNbrRMDCapable.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMplsRsvpTeNbrRMDCapable.setStatus(_A)
class _FsMplsRsvpTeNbrEncapsType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ipencap',1),('udpencap',2),('both',3)))
_FsMplsRsvpTeNbrEncapsType_Type.__name__=_D
_FsMplsRsvpTeNbrEncapsType_Object=MibTableColumn
fsMplsRsvpTeNbrEncapsType=_FsMplsRsvpTeNbrEncapsType_Object((1,3,6,1,4,1,2076,13,2,1,3,1,5),_FsMplsRsvpTeNbrEncapsType_Type())
fsMplsRsvpTeNbrEncapsType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMplsRsvpTeNbrEncapsType.setStatus(_A)
class _FsMplsRsvpTeNbrHelloSupport_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_FsMplsRsvpTeNbrHelloSupport_Type.__name__=_D
_FsMplsRsvpTeNbrHelloSupport_Object=MibTableColumn
fsMplsRsvpTeNbrHelloSupport=_FsMplsRsvpTeNbrHelloSupport_Object((1,3,6,1,4,1,2076,13,2,1,3,1,6),_FsMplsRsvpTeNbrHelloSupport_Type())
fsMplsRsvpTeNbrHelloSupport.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMplsRsvpTeNbrHelloSupport.setStatus(_A)
class _FsMplsRsvpTeNbrHelloState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('unknown',0),('supported',1),(_T,2),('supportReset',3)))
_FsMplsRsvpTeNbrHelloState_Type.__name__=_D
_FsMplsRsvpTeNbrHelloState_Object=MibTableColumn
fsMplsRsvpTeNbrHelloState=_FsMplsRsvpTeNbrHelloState_Object((1,3,6,1,4,1,2076,13,2,1,3,1,7),_FsMplsRsvpTeNbrHelloState_Type())
fsMplsRsvpTeNbrHelloState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsRsvpTeNbrHelloState.setStatus(_A)
class _FsMplsRsvpTeNbrHelloRelation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('passive',2)))
_FsMplsRsvpTeNbrHelloRelation_Type.__name__=_D
_FsMplsRsvpTeNbrHelloRelation_Object=MibTableColumn
fsMplsRsvpTeNbrHelloRelation=_FsMplsRsvpTeNbrHelloRelation_Object((1,3,6,1,4,1,2076,13,2,1,3,1,8),_FsMplsRsvpTeNbrHelloRelation_Type())
fsMplsRsvpTeNbrHelloRelation.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsRsvpTeNbrHelloRelation.setStatus(_A)
_FsMplsRsvpTeNbrSrcInstInfo_Type=Integer32
_FsMplsRsvpTeNbrSrcInstInfo_Object=MibTableColumn
fsMplsRsvpTeNbrSrcInstInfo=_FsMplsRsvpTeNbrSrcInstInfo_Object((1,3,6,1,4,1,2076,13,2,1,3,1,9),_FsMplsRsvpTeNbrSrcInstInfo_Type())
fsMplsRsvpTeNbrSrcInstInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsRsvpTeNbrSrcInstInfo.setStatus(_A)
_FsMplsRsvpTeNbrDestInstInfo_Type=Integer32
_FsMplsRsvpTeNbrDestInstInfo_Object=MibTableColumn
fsMplsRsvpTeNbrDestInstInfo=_FsMplsRsvpTeNbrDestInstInfo_Object((1,3,6,1,4,1,2076,13,2,1,3,1,10),_FsMplsRsvpTeNbrDestInstInfo_Type())
fsMplsRsvpTeNbrDestInstInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsRsvpTeNbrDestInstInfo.setStatus(_A)
_FsMplsRsvpTeNbrCreationTime_Type=TimeStamp
_FsMplsRsvpTeNbrCreationTime_Object=MibTableColumn
fsMplsRsvpTeNbrCreationTime=_FsMplsRsvpTeNbrCreationTime_Object((1,3,6,1,4,1,2076,13,2,1,3,1,11),_FsMplsRsvpTeNbrCreationTime_Type())
fsMplsRsvpTeNbrCreationTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsRsvpTeNbrCreationTime.setStatus(_A)
_FsMplsRsvpTeNbrLclRprDetectionTime_Type=TimeStamp
_FsMplsRsvpTeNbrLclRprDetectionTime_Object=MibTableColumn
fsMplsRsvpTeNbrLclRprDetectionTime=_FsMplsRsvpTeNbrLclRprDetectionTime_Object((1,3,6,1,4,1,2076,13,2,1,3,1,12),_FsMplsRsvpTeNbrLclRprDetectionTime_Type())
fsMplsRsvpTeNbrLclRprDetectionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsRsvpTeNbrLclRprDetectionTime.setStatus(_A)
_FsMplsRsvpTeNbrNumTunnels_Type=Counter32
_FsMplsRsvpTeNbrNumTunnels_Object=MibTableColumn
fsMplsRsvpTeNbrNumTunnels=_FsMplsRsvpTeNbrNumTunnels_Object((1,3,6,1,4,1,2076,13,2,1,3,1,13),_FsMplsRsvpTeNbrNumTunnels_Type())
fsMplsRsvpTeNbrNumTunnels.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsRsvpTeNbrNumTunnels.setStatus(_A)
_FsMplsRsvpTeNbrStatus_Type=RowStatus
_FsMplsRsvpTeNbrStatus_Object=MibTableColumn
fsMplsRsvpTeNbrStatus=_FsMplsRsvpTeNbrStatus_Object((1,3,6,1,4,1,2076,13,2,1,3,1,14),_FsMplsRsvpTeNbrStatus_Type())
fsMplsRsvpTeNbrStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMplsRsvpTeNbrStatus.setStatus(_A)
class _FsMplsRsvpTeNbrGrRecoveryPathCapability_Type(Bits):namedValues=NamedValues(*((_V,0),(_W,1),(_X,2)))
_FsMplsRsvpTeNbrGrRecoveryPathCapability_Type.__name__=_K
_FsMplsRsvpTeNbrGrRecoveryPathCapability_Object=MibTableColumn
fsMplsRsvpTeNbrGrRecoveryPathCapability=_FsMplsRsvpTeNbrGrRecoveryPathCapability_Object((1,3,6,1,4,1,2076,13,2,1,3,1,15),_FsMplsRsvpTeNbrGrRecoveryPathCapability_Type())
fsMplsRsvpTeNbrGrRecoveryPathCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsRsvpTeNbrGrRecoveryPathCapability.setStatus(_A)
_FsMplsRsvpTeNbrGrRestartTime_Type=Integer32
_FsMplsRsvpTeNbrGrRestartTime_Object=MibTableColumn
fsMplsRsvpTeNbrGrRestartTime=_FsMplsRsvpTeNbrGrRestartTime_Object((1,3,6,1,4,1,2076,13,2,1,3,1,16),_FsMplsRsvpTeNbrGrRestartTime_Type())
fsMplsRsvpTeNbrGrRestartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsRsvpTeNbrGrRestartTime.setStatus(_A)
_FsMplsRsvpTeNbrGrRecoveryTime_Type=Integer32
_FsMplsRsvpTeNbrGrRecoveryTime_Object=MibTableColumn
fsMplsRsvpTeNbrGrRecoveryTime=_FsMplsRsvpTeNbrGrRecoveryTime_Object((1,3,6,1,4,1,2076,13,2,1,3,1,17),_FsMplsRsvpTeNbrGrRecoveryTime_Type())
fsMplsRsvpTeNbrGrRecoveryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsRsvpTeNbrGrRecoveryTime.setStatus(_A)
_FsMplsRsvpTeNbrGrProgressStatus_Type=Integer32
_FsMplsRsvpTeNbrGrProgressStatus_Object=MibTableColumn
fsMplsRsvpTeNbrGrProgressStatus=_FsMplsRsvpTeNbrGrProgressStatus_Object((1,3,6,1,4,1,2076,13,2,1,3,1,18),_FsMplsRsvpTeNbrGrProgressStatus_Type())
fsMplsRsvpTeNbrGrProgressStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsRsvpTeNbrGrProgressStatus.setStatus(_A)
class _FsMplsRsvpTeNbrStorageType_Type(StorageType):defaultValue=3
_FsMplsRsvpTeNbrStorageType_Type.__name__=_L
_FsMplsRsvpTeNbrStorageType_Object=MibTableColumn
fsMplsRsvpTeNbrStorageType=_FsMplsRsvpTeNbrStorageType_Object((1,3,6,1,4,1,2076,13,2,1,3,1,19),_FsMplsRsvpTeNbrStorageType_Type())
fsMplsRsvpTeNbrStorageType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMplsRsvpTeNbrStorageType.setStatus(_A)
_FsMplsRsvpTeGenObjects_ObjectIdentity=ObjectIdentity
fsMplsRsvpTeGenObjects=_FsMplsRsvpTeGenObjects_ObjectIdentity((1,3,6,1,4,1,2076,13,2,2))
_FsMplsRsvpTeLsrID_Type=MplsLsrIdentifier
_FsMplsRsvpTeLsrID_Object=MibScalar
fsMplsRsvpTeLsrID=_FsMplsRsvpTeLsrID_Object((1,3,6,1,4,1,2076,13,2,2,1),_FsMplsRsvpTeLsrID_Type())
fsMplsRsvpTeLsrID.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMplsRsvpTeLsrID.setStatus(_A)
class _FsMplsRsvpTeMaxTnls_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsMplsRsvpTeMaxTnls_Type.__name__=_D
_FsMplsRsvpTeMaxTnls_Object=MibScalar
fsMplsRsvpTeMaxTnls=_FsMplsRsvpTeMaxTnls_Object((1,3,6,1,4,1,2076,13,2,2,2),_FsMplsRsvpTeMaxTnls_Type())
fsMplsRsvpTeMaxTnls.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMplsRsvpTeMaxTnls.setStatus(_A)
class _FsMplsRsvpTeMaxErhopsPerTnl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsMplsRsvpTeMaxErhopsPerTnl_Type.__name__=_D
_FsMplsRsvpTeMaxErhopsPerTnl_Object=MibScalar
fsMplsRsvpTeMaxErhopsPerTnl=_FsMplsRsvpTeMaxErhopsPerTnl_Object((1,3,6,1,4,1,2076,13,2,2,3),_FsMplsRsvpTeMaxErhopsPerTnl_Type())
fsMplsRsvpTeMaxErhopsPerTnl.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMplsRsvpTeMaxErhopsPerTnl.setStatus(_A)
class _FsMplsRsvpTeMaxActRoutePerTnl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsMplsRsvpTeMaxActRoutePerTnl_Type.__name__=_D
_FsMplsRsvpTeMaxActRoutePerTnl_Object=MibScalar
fsMplsRsvpTeMaxActRoutePerTnl=_FsMplsRsvpTeMaxActRoutePerTnl_Object((1,3,6,1,4,1,2076,13,2,2,4),_FsMplsRsvpTeMaxActRoutePerTnl_Type())
fsMplsRsvpTeMaxActRoutePerTnl.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMplsRsvpTeMaxActRoutePerTnl.setStatus(_A)
class _FsMplsRsvpTeMaxIfaces_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsMplsRsvpTeMaxIfaces_Type.__name__=_D
_FsMplsRsvpTeMaxIfaces_Object=MibScalar
fsMplsRsvpTeMaxIfaces=_FsMplsRsvpTeMaxIfaces_Object((1,3,6,1,4,1,2076,13,2,2,5),_FsMplsRsvpTeMaxIfaces_Type())
fsMplsRsvpTeMaxIfaces.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMplsRsvpTeMaxIfaces.setStatus(_A)
class _FsMplsRsvpTeMaxNbrs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsMplsRsvpTeMaxNbrs_Type.__name__=_D
_FsMplsRsvpTeMaxNbrs_Object=MibScalar
fsMplsRsvpTeMaxNbrs=_FsMplsRsvpTeMaxNbrs_Object((1,3,6,1,4,1,2076,13,2,2,6),_FsMplsRsvpTeMaxNbrs_Type())
fsMplsRsvpTeMaxNbrs.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMplsRsvpTeMaxNbrs.setStatus(_A)
class _FsMplsRsvpTeSockSupprtd_Type(TruthValue):defaultValue=1
_FsMplsRsvpTeSockSupprtd_Type.__name__=_G
_FsMplsRsvpTeSockSupprtd_Object=MibScalar
fsMplsRsvpTeSockSupprtd=_FsMplsRsvpTeSockSupprtd_Object((1,3,6,1,4,1,2076,13,2,2,7),_FsMplsRsvpTeSockSupprtd_Type())
fsMplsRsvpTeSockSupprtd.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMplsRsvpTeSockSupprtd.setStatus(_A)
class _FsMplsRsvpTeHelloSupprtd_Type(TruthValue):defaultValue=2
_FsMplsRsvpTeHelloSupprtd_Type.__name__=_G
_FsMplsRsvpTeHelloSupprtd_Object=MibScalar
fsMplsRsvpTeHelloSupprtd=_FsMplsRsvpTeHelloSupprtd_Object((1,3,6,1,4,1,2076,13,2,2,8),_FsMplsRsvpTeHelloSupprtd_Type())
fsMplsRsvpTeHelloSupprtd.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMplsRsvpTeHelloSupprtd.setStatus(_A)
class _FsMplsRsvpTeHelloIntervalTime_Type(Integer32):defaultValue=10000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,30000))
_FsMplsRsvpTeHelloIntervalTime_Type.__name__=_D
_FsMplsRsvpTeHelloIntervalTime_Object=MibScalar
fsMplsRsvpTeHelloIntervalTime=_FsMplsRsvpTeHelloIntervalTime_Object((1,3,6,1,4,1,2076,13,2,2,9),_FsMplsRsvpTeHelloIntervalTime_Type())
fsMplsRsvpTeHelloIntervalTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMplsRsvpTeHelloIntervalTime.setStatus(_A)
class _FsMplsRsvpTeRRCapable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_FsMplsRsvpTeRRCapable_Type.__name__=_D
_FsMplsRsvpTeRRCapable_Object=MibScalar
fsMplsRsvpTeRRCapable=_FsMplsRsvpTeRRCapable_Object((1,3,6,1,4,1,2076,13,2,2,10),_FsMplsRsvpTeRRCapable_Type())
fsMplsRsvpTeRRCapable.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMplsRsvpTeRRCapable.setStatus(_A)
class _FsMplsRsvpTeMsgIdCapable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_FsMplsRsvpTeMsgIdCapable_Type.__name__=_D
_FsMplsRsvpTeMsgIdCapable_Object=MibScalar
fsMplsRsvpTeMsgIdCapable=_FsMplsRsvpTeMsgIdCapable_Object((1,3,6,1,4,1,2076,13,2,2,11),_FsMplsRsvpTeMsgIdCapable_Type())
fsMplsRsvpTeMsgIdCapable.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMplsRsvpTeMsgIdCapable.setStatus(_A)
class _FsMplsRsvpTeRMDPolicyObject_Type(Bits):namedValues=NamedValues(*(('path',0),('resv',1),('pathErr',2),('resvErr',3),('pathTear',4),('resvTear',5),('notify',6)))
_FsMplsRsvpTeRMDPolicyObject_Type.__name__=_K
_FsMplsRsvpTeRMDPolicyObject_Object=MibScalar
fsMplsRsvpTeRMDPolicyObject=_FsMplsRsvpTeRMDPolicyObject_Object((1,3,6,1,4,1,2076,13,2,2,12),_FsMplsRsvpTeRMDPolicyObject_Type())
fsMplsRsvpTeRMDPolicyObject.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMplsRsvpTeRMDPolicyObject.setStatus(_A)
class _FsMplsRsvpTeGenLblSpaceMinLbl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100001,160000))
_FsMplsRsvpTeGenLblSpaceMinLbl_Type.__name__=_D
_FsMplsRsvpTeGenLblSpaceMinLbl_Object=MibScalar
fsMplsRsvpTeGenLblSpaceMinLbl=_FsMplsRsvpTeGenLblSpaceMinLbl_Object((1,3,6,1,4,1,2076,13,2,2,13),_FsMplsRsvpTeGenLblSpaceMinLbl_Type())
fsMplsRsvpTeGenLblSpaceMinLbl.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMplsRsvpTeGenLblSpaceMinLbl.setStatus(_A)
class _FsMplsRsvpTeGenLblSpaceMaxLbl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100001,160000))
_FsMplsRsvpTeGenLblSpaceMaxLbl_Type.__name__=_D
_FsMplsRsvpTeGenLblSpaceMaxLbl_Object=MibScalar
fsMplsRsvpTeGenLblSpaceMaxLbl=_FsMplsRsvpTeGenLblSpaceMaxLbl_Object((1,3,6,1,4,1,2076,13,2,2,14),_FsMplsRsvpTeGenLblSpaceMaxLbl_Type())
fsMplsRsvpTeGenLblSpaceMaxLbl.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMplsRsvpTeGenLblSpaceMaxLbl.setStatus(_A)
class _FsMplsRsvpTeGenDebugFlag_Type(Unsigned32):defaultValue=0
_FsMplsRsvpTeGenDebugFlag_Type.__name__=_F
_FsMplsRsvpTeGenDebugFlag_Object=MibScalar
fsMplsRsvpTeGenDebugFlag=_FsMplsRsvpTeGenDebugFlag_Object((1,3,6,1,4,1,2076,13,2,2,15),_FsMplsRsvpTeGenDebugFlag_Type())
fsMplsRsvpTeGenDebugFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMplsRsvpTeGenDebugFlag.setStatus(_A)
class _FsMplsRsvpTeGenPduDumpLevel_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4)));namedValues=NamedValues(*(('none',0),('min',1),('max',2),('hdr',4)))
_FsMplsRsvpTeGenPduDumpLevel_Type.__name__=_D
_FsMplsRsvpTeGenPduDumpLevel_Object=MibScalar
fsMplsRsvpTeGenPduDumpLevel=_FsMplsRsvpTeGenPduDumpLevel_Object((1,3,6,1,4,1,2076,13,2,2,16),_FsMplsRsvpTeGenPduDumpLevel_Type())
fsMplsRsvpTeGenPduDumpLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMplsRsvpTeGenPduDumpLevel.setStatus(_A)
_FsMplsRsvpTeGenPduDumpMsgType_Type=Integer32
_FsMplsRsvpTeGenPduDumpMsgType_Object=MibScalar
fsMplsRsvpTeGenPduDumpMsgType=_FsMplsRsvpTeGenPduDumpMsgType_Object((1,3,6,1,4,1,2076,13,2,2,17),_FsMplsRsvpTeGenPduDumpMsgType_Type())
fsMplsRsvpTeGenPduDumpMsgType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMplsRsvpTeGenPduDumpMsgType.setStatus(_A)
_FsMplsRsvpTeGenPduDumpDirection_Type=Integer32
_FsMplsRsvpTeGenPduDumpDirection_Object=MibScalar
fsMplsRsvpTeGenPduDumpDirection=_FsMplsRsvpTeGenPduDumpDirection_Object((1,3,6,1,4,1,2076,13,2,2,18),_FsMplsRsvpTeGenPduDumpDirection_Type())
fsMplsRsvpTeGenPduDumpDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMplsRsvpTeGenPduDumpDirection.setStatus(_A)
class _FsMplsRsvpTeOperStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('up',1),('down',2),('testing',3),('upinprgrs',4),('downinprgrs',5)))
_FsMplsRsvpTeOperStatus_Type.__name__=_D
_FsMplsRsvpTeOperStatus_Object=MibScalar
fsMplsRsvpTeOperStatus=_FsMplsRsvpTeOperStatus_Object((1,3,6,1,4,1,2076,13,2,2,19),_FsMplsRsvpTeOperStatus_Type())
fsMplsRsvpTeOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMplsRsvpTeOperStatus.setStatus(_A)
class _FsMplsRsvpTeOverRideOption_Type(TruthValue):defaultValue=1
_FsMplsRsvpTeOverRideOption_Type.__name__=_G
_FsMplsRsvpTeOverRideOption_Object=MibScalar
fsMplsRsvpTeOverRideOption=_FsMplsRsvpTeOverRideOption_Object((1,3,6,1,4,1,2076,13,2,2,20),_FsMplsRsvpTeOverRideOption_Type())
fsMplsRsvpTeOverRideOption.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMplsRsvpTeOverRideOption.setStatus(_A)
class _FsMplsRsvpTeMinTnlsWithMsgId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsMplsRsvpTeMinTnlsWithMsgId_Type.__name__=_F
_FsMplsRsvpTeMinTnlsWithMsgId_Object=MibScalar
fsMplsRsvpTeMinTnlsWithMsgId=_FsMplsRsvpTeMinTnlsWithMsgId_Object((1,3,6,1,4,1,2076,13,2,2,21),_FsMplsRsvpTeMinTnlsWithMsgId_Type())
fsMplsRsvpTeMinTnlsWithMsgId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMplsRsvpTeMinTnlsWithMsgId.setStatus(_A)
class _FsMplsRsvpTeNotificationEnabled_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_FsMplsRsvpTeNotificationEnabled_Type.__name__=_D
_FsMplsRsvpTeNotificationEnabled_Object=MibScalar
fsMplsRsvpTeNotificationEnabled=_FsMplsRsvpTeNotificationEnabled_Object((1,3,6,1,4,1,2076,13,2,2,22),_FsMplsRsvpTeNotificationEnabled_Type())
fsMplsRsvpTeNotificationEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMplsRsvpTeNotificationEnabled.setStatus(_A)
class _FsMplsRsvpTeNotifyMsgRetransmitIntvl_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,30000))
_FsMplsRsvpTeNotifyMsgRetransmitIntvl_Type.__name__=_F
_FsMplsRsvpTeNotifyMsgRetransmitIntvl_Object=MibScalar
fsMplsRsvpTeNotifyMsgRetransmitIntvl=_FsMplsRsvpTeNotifyMsgRetransmitIntvl_Object((1,3,6,1,4,1,2076,13,2,2,23),_FsMplsRsvpTeNotifyMsgRetransmitIntvl_Type())
fsMplsRsvpTeNotifyMsgRetransmitIntvl.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMplsRsvpTeNotifyMsgRetransmitIntvl.setStatus(_A)
class _FsMplsRsvpTeNotifyMsgRetransmitDecay_Type(Unsigned32):defaultValue=0
_FsMplsRsvpTeNotifyMsgRetransmitDecay_Type.__name__=_F
_FsMplsRsvpTeNotifyMsgRetransmitDecay_Object=MibScalar
fsMplsRsvpTeNotifyMsgRetransmitDecay=_FsMplsRsvpTeNotifyMsgRetransmitDecay_Object((1,3,6,1,4,1,2076,13,2,2,24),_FsMplsRsvpTeNotifyMsgRetransmitDecay_Type())
fsMplsRsvpTeNotifyMsgRetransmitDecay.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMplsRsvpTeNotifyMsgRetransmitDecay.setStatus(_A)
class _FsMplsRsvpTeNotifyMsgRetransmitLimit_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_FsMplsRsvpTeNotifyMsgRetransmitLimit_Type.__name__=_F
_FsMplsRsvpTeNotifyMsgRetransmitLimit_Object=MibScalar
fsMplsRsvpTeNotifyMsgRetransmitLimit=_FsMplsRsvpTeNotifyMsgRetransmitLimit_Object((1,3,6,1,4,1,2076,13,2,2,25),_FsMplsRsvpTeNotifyMsgRetransmitLimit_Type())
fsMplsRsvpTeNotifyMsgRetransmitLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMplsRsvpTeNotifyMsgRetransmitLimit.setStatus(_A)
class _FsMplsRsvpTeAdminStatusTimeIntvl_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_FsMplsRsvpTeAdminStatusTimeIntvl_Type.__name__=_F
_FsMplsRsvpTeAdminStatusTimeIntvl_Object=MibScalar
fsMplsRsvpTeAdminStatusTimeIntvl=_FsMplsRsvpTeAdminStatusTimeIntvl_Object((1,3,6,1,4,1,2076,13,2,2,26),_FsMplsRsvpTeAdminStatusTimeIntvl_Type())
fsMplsRsvpTeAdminStatusTimeIntvl.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMplsRsvpTeAdminStatusTimeIntvl.setStatus(_A)
class _FsMplsRsvpTePathStateRemovedSupport_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_FsMplsRsvpTePathStateRemovedSupport_Type.__name__=_D
_FsMplsRsvpTePathStateRemovedSupport_Object=MibScalar
fsMplsRsvpTePathStateRemovedSupport=_FsMplsRsvpTePathStateRemovedSupport_Object((1,3,6,1,4,1,2076,13,2,2,27),_FsMplsRsvpTePathStateRemovedSupport_Type())
fsMplsRsvpTePathStateRemovedSupport.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMplsRsvpTePathStateRemovedSupport.setStatus(_A)
class _FsMplsRsvpTeLabelSetEnabled_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_FsMplsRsvpTeLabelSetEnabled_Type.__name__=_D
_FsMplsRsvpTeLabelSetEnabled_Object=MibScalar
fsMplsRsvpTeLabelSetEnabled=_FsMplsRsvpTeLabelSetEnabled_Object((1,3,6,1,4,1,2076,13,2,2,28),_FsMplsRsvpTeLabelSetEnabled_Type())
fsMplsRsvpTeLabelSetEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMplsRsvpTeLabelSetEnabled.setStatus(_A)
class _FsMplsRsvpTeAdminStatusCapability_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_FsMplsRsvpTeAdminStatusCapability_Type.__name__=_D
_FsMplsRsvpTeAdminStatusCapability_Object=MibScalar
fsMplsRsvpTeAdminStatusCapability=_FsMplsRsvpTeAdminStatusCapability_Object((1,3,6,1,4,1,2076,13,2,2,29),_FsMplsRsvpTeAdminStatusCapability_Type())
fsMplsRsvpTeAdminStatusCapability.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMplsRsvpTeAdminStatusCapability.setStatus(_A)
class _FsMplsRsvpTeGrCapability_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('full',2),('helper',3)))
_FsMplsRsvpTeGrCapability_Type.__name__=_D
_FsMplsRsvpTeGrCapability_Object=MibScalar
fsMplsRsvpTeGrCapability=_FsMplsRsvpTeGrCapability_Object((1,3,6,1,4,1,2076,13,2,2,30),_FsMplsRsvpTeGrCapability_Type())
fsMplsRsvpTeGrCapability.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMplsRsvpTeGrCapability.setStatus(_A)
class _FsMplsRsvpTeGrRecoveryPathCapability_Type(Bits):defaultHexValue='';namedValues=NamedValues(*((_V,0),(_W,1),(_X,2)))
_FsMplsRsvpTeGrRecoveryPathCapability_Type.__name__=_K
_FsMplsRsvpTeGrRecoveryPathCapability_Object=MibScalar
fsMplsRsvpTeGrRecoveryPathCapability=_FsMplsRsvpTeGrRecoveryPathCapability_Object((1,3,6,1,4,1,2076,13,2,2,31),_FsMplsRsvpTeGrRecoveryPathCapability_Type())
fsMplsRsvpTeGrRecoveryPathCapability.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMplsRsvpTeGrRecoveryPathCapability.setStatus(_A)
class _FsMplsRsvpTeGrRestartTime_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,3600))
_FsMplsRsvpTeGrRestartTime_Type.__name__=_D
_FsMplsRsvpTeGrRestartTime_Object=MibScalar
fsMplsRsvpTeGrRestartTime=_FsMplsRsvpTeGrRestartTime_Object((1,3,6,1,4,1,2076,13,2,2,32),_FsMplsRsvpTeGrRestartTime_Type())
fsMplsRsvpTeGrRestartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMplsRsvpTeGrRestartTime.setStatus(_A)
class _FsMplsRsvpTeGrRecoveryTime_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,480))
_FsMplsRsvpTeGrRecoveryTime_Type.__name__=_D
_FsMplsRsvpTeGrRecoveryTime_Object=MibScalar
fsMplsRsvpTeGrRecoveryTime=_FsMplsRsvpTeGrRecoveryTime_Object((1,3,6,1,4,1,2076,13,2,2,33),_FsMplsRsvpTeGrRecoveryTime_Type())
fsMplsRsvpTeGrRecoveryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMplsRsvpTeGrRecoveryTime.setStatus(_A)
_FsMplsRsvpTeGrProgressStatus_Type=Integer32
_FsMplsRsvpTeGrProgressStatus_Object=MibScalar
fsMplsRsvpTeGrProgressStatus=_FsMplsRsvpTeGrProgressStatus_Object((1,3,6,1,4,1,2076,13,2,2,34),_FsMplsRsvpTeGrProgressStatus_Type())
fsMplsRsvpTeGrProgressStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsRsvpTeGrProgressStatus.setStatus(_A)
class _FsMplsRsvpTeReoptimizeTime_Type(Integer32):defaultValue=60
_FsMplsRsvpTeReoptimizeTime_Type.__name__=_D
_FsMplsRsvpTeReoptimizeTime_Object=MibScalar
fsMplsRsvpTeReoptimizeTime=_FsMplsRsvpTeReoptimizeTime_Object((1,3,6,1,4,1,2076,13,2,2,35),_FsMplsRsvpTeReoptimizeTime_Type())
fsMplsRsvpTeReoptimizeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMplsRsvpTeReoptimizeTime.setStatus(_A)
class _FsMplsRsvpTeEroCacheTime_Type(Integer32):defaultValue=5
_FsMplsRsvpTeEroCacheTime_Type.__name__=_D
_FsMplsRsvpTeEroCacheTime_Object=MibScalar
fsMplsRsvpTeEroCacheTime=_FsMplsRsvpTeEroCacheTime_Object((1,3,6,1,4,1,2076,13,2,2,36),_FsMplsRsvpTeEroCacheTime_Type())
fsMplsRsvpTeEroCacheTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMplsRsvpTeEroCacheTime.setStatus(_A)
_FsMplsRsvpTeReoptLinkMaintenance_Type=Integer32
_FsMplsRsvpTeReoptLinkMaintenance_Object=MibScalar
fsMplsRsvpTeReoptLinkMaintenance=_FsMplsRsvpTeReoptLinkMaintenance_Object((1,3,6,1,4,1,2076,13,2,2,37),_FsMplsRsvpTeReoptLinkMaintenance_Type())
fsMplsRsvpTeReoptLinkMaintenance.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMplsRsvpTeReoptLinkMaintenance.setStatus(_A)
_FsMplsRsvpTeReoptNodeMaintenance_Type=Integer32
_FsMplsRsvpTeReoptNodeMaintenance_Object=MibScalar
fsMplsRsvpTeReoptNodeMaintenance=_FsMplsRsvpTeReoptNodeMaintenance_Object((1,3,6,1,4,1,2076,13,2,2,38),_FsMplsRsvpTeReoptNodeMaintenance_Type())
fsMplsRsvpTeReoptNodeMaintenance.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMplsRsvpTeReoptNodeMaintenance.setStatus(_A)
fsMplsRsvpTeIfEntry.registerAugmentions((_J,_Y))
fsMplsRsvpTeIfStatsEntry.setIndexNames(*fsMplsRsvpTeIfEntry.getIndexNames())
mibBuilder.exportSymbols(_J,**{'MplsLsrIdentifier':MplsLsrIdentifier,_O:AtmVpIdentifier,_P:AtmVcIdentifier,'fsMplsRsvpTeMIB':fsMplsRsvpTeMIB,'fsMplsRsvpTeObjects':fsMplsRsvpTeObjects,'fsMplsRsvpTeIfTable':fsMplsRsvpTeIfTable,'fsMplsRsvpTeIfEntry':fsMplsRsvpTeIfEntry,_N:fsMplsRsvpTeIfIndex,'fsMplsRsvpTeIfLblSpace':fsMplsRsvpTeIfLblSpace,'fsMplsRsvpTeIfLblType':fsMplsRsvpTeIfLblType,'fsMplsRsvpTeAtmMergeCap':fsMplsRsvpTeAtmMergeCap,'fsMplsRsvpTeAtmVcDirection':fsMplsRsvpTeAtmVcDirection,'fsMplsRsvpTeAtmMinVpi':fsMplsRsvpTeAtmMinVpi,'fsMplsRsvpTeAtmMinVci':fsMplsRsvpTeAtmMinVci,'fsMplsRsvpTeAtmMaxVpi':fsMplsRsvpTeAtmMaxVpi,'fsMplsRsvpTeAtmMaxVci':fsMplsRsvpTeAtmMaxVci,'fsMplsRsvpTeIfMtu':fsMplsRsvpTeIfMtu,'fsMplsRsvpTeIfUdpNbrs':fsMplsRsvpTeIfUdpNbrs,'fsMplsRsvpTeIfIpNbrs':fsMplsRsvpTeIfIpNbrs,'fsMplsRsvpTeIfNbrs':fsMplsRsvpTeIfNbrs,'fsMplsRsvpTeIfRefreshMultiple':fsMplsRsvpTeIfRefreshMultiple,'fsMplsRsvpTeIfTTL':fsMplsRsvpTeIfTTL,'fsMplsRsvpTeIfRefreshInterval':fsMplsRsvpTeIfRefreshInterval,'fsMplsRsvpTeIfRouteDelay':fsMplsRsvpTeIfRouteDelay,'fsMplsRsvpTeIfUdpRequired':fsMplsRsvpTeIfUdpRequired,'fsMplsRsvpTeIfHelloSupported':fsMplsRsvpTeIfHelloSupported,'fsMplsRsvpTeIfLinkAttr':fsMplsRsvpTeIfLinkAttr,'fsMplsRsvpTeIfStatus':fsMplsRsvpTeIfStatus,'fsMplsRsvpTeIfPlrId':fsMplsRsvpTeIfPlrId,'fsMplsRsvpTeIfAvoidNodeId':fsMplsRsvpTeIfAvoidNodeId,'fsMplsRsvpTeIfStorageType':fsMplsRsvpTeIfStorageType,'fsMplsRsvpTeIfStatsTable':fsMplsRsvpTeIfStatsTable,_Y:fsMplsRsvpTeIfStatsEntry,'fsMplsRsvpTeIfNumTnls':fsMplsRsvpTeIfNumTnls,'fsMplsRsvpTeIfNumMsgSent':fsMplsRsvpTeIfNumMsgSent,'fsMplsRsvpTeIfNumMsgRcvd':fsMplsRsvpTeIfNumMsgRcvd,'fsMplsRsvpTeIfNumHelloSent':fsMplsRsvpTeIfNumHelloSent,'fsMplsRsvpTeIfNumHelloRcvd':fsMplsRsvpTeIfNumHelloRcvd,'fsMplsRsvpTeIfNumPathErrSent':fsMplsRsvpTeIfNumPathErrSent,'fsMplsRsvpTeIfNumPathErrRcvd':fsMplsRsvpTeIfNumPathErrRcvd,'fsMplsRsvpTeIfNumPathTearSent':fsMplsRsvpTeIfNumPathTearSent,'fsMplsRsvpTeIfNumPathTearRcvd':fsMplsRsvpTeIfNumPathTearRcvd,'fsMplsRsvpTeIfNumResvErrSent':fsMplsRsvpTeIfNumResvErrSent,'fsMplsRsvpTeIfNumResvErrRcvd':fsMplsRsvpTeIfNumResvErrRcvd,'fsMplsRsvpTeIfNumResvTearSent':fsMplsRsvpTeIfNumResvTearSent,'fsMplsRsvpTeIfNumResvTearRcvd':fsMplsRsvpTeIfNumResvTearRcvd,'fsMplsRsvpTeIfNumResvConfSent':fsMplsRsvpTeIfNumResvConfSent,'fsMplsRsvpTeIfNumResvConfRcvd':fsMplsRsvpTeIfNumResvConfRcvd,'fsMplsRsvpTeIfNumBundleMsgSent':fsMplsRsvpTeIfNumBundleMsgSent,'fsMplsRsvpTeIfNumBundleMsgRcvd':fsMplsRsvpTeIfNumBundleMsgRcvd,'fsMplsRsvpTeIfNumSRefreshMsgSent':fsMplsRsvpTeIfNumSRefreshMsgSent,'fsMplsRsvpTeIfNumSRefreshMsgRcvd':fsMplsRsvpTeIfNumSRefreshMsgRcvd,'fsMplsRsvpTeIfNumPathSent':fsMplsRsvpTeIfNumPathSent,'fsMplsRsvpTeIfNumPathRcvd':fsMplsRsvpTeIfNumPathRcvd,'fsMplsRsvpTeIfNumResvSent':fsMplsRsvpTeIfNumResvSent,'fsMplsRsvpTeIfNumResvRcvd':fsMplsRsvpTeIfNumResvRcvd,'fsMplsRsvpTeIfNumNotifyMsgSent':fsMplsRsvpTeIfNumNotifyMsgSent,'fsMplsRsvpTeIfNumNotifyMsgRcvd':fsMplsRsvpTeIfNumNotifyMsgRcvd,'fsMplsRsvpTeIfNumRecoveryPathSent':fsMplsRsvpTeIfNumRecoveryPathSent,'fsMplsRsvpTeIfNumRecoveryPathRcvd':fsMplsRsvpTeIfNumRecoveryPathRcvd,'fsMplsRsvpTeIfNumPathSentWithRecoveryLbl':fsMplsRsvpTeIfNumPathSentWithRecoveryLbl,'fsMplsRsvpTeIfNumPathRcvdWithRecoveryLbl':fsMplsRsvpTeIfNumPathRcvdWithRecoveryLbl,'fsMplsRsvpTeIfNumPathSentWithSuggestedLbl':fsMplsRsvpTeIfNumPathSentWithSuggestedLbl,'fsMplsRsvpTeIfNumPathRcvdWithSuggestedLbl':fsMplsRsvpTeIfNumPathRcvdWithSuggestedLbl,'fsMplsRsvpTeIfNumHelloSentWithRestartCap':fsMplsRsvpTeIfNumHelloSentWithRestartCap,'fsMplsRsvpTeIfNumHelloRcvdWithRestartCap':fsMplsRsvpTeIfNumHelloRcvdWithRestartCap,'fsMplsRsvpTeIfNumHelloSentWithCapability':fsMplsRsvpTeIfNumHelloSentWithCapability,'fsMplsRsvpTeIfNumHelloRcvdWithCapability':fsMplsRsvpTeIfNumHelloRcvdWithCapability,'fsMplsRsvpTeIfNumPktDiscrded':fsMplsRsvpTeIfNumPktDiscrded,'fsMplsRsvpTeNbrTable':fsMplsRsvpTeNbrTable,'fsMplsRsvpTeNbrEntry':fsMplsRsvpTeNbrEntry,_U:fsMplsRsvpTeNbrIfAddr,'fsMplsRsvpTeNbrRRCapable':fsMplsRsvpTeNbrRRCapable,'fsMplsRsvpTeNbrRRState':fsMplsRsvpTeNbrRRState,'fsMplsRsvpTeNbrRMDCapable':fsMplsRsvpTeNbrRMDCapable,'fsMplsRsvpTeNbrEncapsType':fsMplsRsvpTeNbrEncapsType,'fsMplsRsvpTeNbrHelloSupport':fsMplsRsvpTeNbrHelloSupport,'fsMplsRsvpTeNbrHelloState':fsMplsRsvpTeNbrHelloState,'fsMplsRsvpTeNbrHelloRelation':fsMplsRsvpTeNbrHelloRelation,'fsMplsRsvpTeNbrSrcInstInfo':fsMplsRsvpTeNbrSrcInstInfo,'fsMplsRsvpTeNbrDestInstInfo':fsMplsRsvpTeNbrDestInstInfo,'fsMplsRsvpTeNbrCreationTime':fsMplsRsvpTeNbrCreationTime,'fsMplsRsvpTeNbrLclRprDetectionTime':fsMplsRsvpTeNbrLclRprDetectionTime,'fsMplsRsvpTeNbrNumTunnels':fsMplsRsvpTeNbrNumTunnels,'fsMplsRsvpTeNbrStatus':fsMplsRsvpTeNbrStatus,'fsMplsRsvpTeNbrGrRecoveryPathCapability':fsMplsRsvpTeNbrGrRecoveryPathCapability,'fsMplsRsvpTeNbrGrRestartTime':fsMplsRsvpTeNbrGrRestartTime,'fsMplsRsvpTeNbrGrRecoveryTime':fsMplsRsvpTeNbrGrRecoveryTime,'fsMplsRsvpTeNbrGrProgressStatus':fsMplsRsvpTeNbrGrProgressStatus,'fsMplsRsvpTeNbrStorageType':fsMplsRsvpTeNbrStorageType,'fsMplsRsvpTeGenObjects':fsMplsRsvpTeGenObjects,'fsMplsRsvpTeLsrID':fsMplsRsvpTeLsrID,'fsMplsRsvpTeMaxTnls':fsMplsRsvpTeMaxTnls,'fsMplsRsvpTeMaxErhopsPerTnl':fsMplsRsvpTeMaxErhopsPerTnl,'fsMplsRsvpTeMaxActRoutePerTnl':fsMplsRsvpTeMaxActRoutePerTnl,'fsMplsRsvpTeMaxIfaces':fsMplsRsvpTeMaxIfaces,'fsMplsRsvpTeMaxNbrs':fsMplsRsvpTeMaxNbrs,'fsMplsRsvpTeSockSupprtd':fsMplsRsvpTeSockSupprtd,'fsMplsRsvpTeHelloSupprtd':fsMplsRsvpTeHelloSupprtd,'fsMplsRsvpTeHelloIntervalTime':fsMplsRsvpTeHelloIntervalTime,'fsMplsRsvpTeRRCapable':fsMplsRsvpTeRRCapable,'fsMplsRsvpTeMsgIdCapable':fsMplsRsvpTeMsgIdCapable,'fsMplsRsvpTeRMDPolicyObject':fsMplsRsvpTeRMDPolicyObject,'fsMplsRsvpTeGenLblSpaceMinLbl':fsMplsRsvpTeGenLblSpaceMinLbl,'fsMplsRsvpTeGenLblSpaceMaxLbl':fsMplsRsvpTeGenLblSpaceMaxLbl,'fsMplsRsvpTeGenDebugFlag':fsMplsRsvpTeGenDebugFlag,'fsMplsRsvpTeGenPduDumpLevel':fsMplsRsvpTeGenPduDumpLevel,'fsMplsRsvpTeGenPduDumpMsgType':fsMplsRsvpTeGenPduDumpMsgType,'fsMplsRsvpTeGenPduDumpDirection':fsMplsRsvpTeGenPduDumpDirection,'fsMplsRsvpTeOperStatus':fsMplsRsvpTeOperStatus,'fsMplsRsvpTeOverRideOption':fsMplsRsvpTeOverRideOption,'fsMplsRsvpTeMinTnlsWithMsgId':fsMplsRsvpTeMinTnlsWithMsgId,'fsMplsRsvpTeNotificationEnabled':fsMplsRsvpTeNotificationEnabled,'fsMplsRsvpTeNotifyMsgRetransmitIntvl':fsMplsRsvpTeNotifyMsgRetransmitIntvl,'fsMplsRsvpTeNotifyMsgRetransmitDecay':fsMplsRsvpTeNotifyMsgRetransmitDecay,'fsMplsRsvpTeNotifyMsgRetransmitLimit':fsMplsRsvpTeNotifyMsgRetransmitLimit,'fsMplsRsvpTeAdminStatusTimeIntvl':fsMplsRsvpTeAdminStatusTimeIntvl,'fsMplsRsvpTePathStateRemovedSupport':fsMplsRsvpTePathStateRemovedSupport,'fsMplsRsvpTeLabelSetEnabled':fsMplsRsvpTeLabelSetEnabled,'fsMplsRsvpTeAdminStatusCapability':fsMplsRsvpTeAdminStatusCapability,'fsMplsRsvpTeGrCapability':fsMplsRsvpTeGrCapability,'fsMplsRsvpTeGrRecoveryPathCapability':fsMplsRsvpTeGrRecoveryPathCapability,'fsMplsRsvpTeGrRestartTime':fsMplsRsvpTeGrRestartTime,'fsMplsRsvpTeGrRecoveryTime':fsMplsRsvpTeGrRecoveryTime,'fsMplsRsvpTeGrProgressStatus':fsMplsRsvpTeGrProgressStatus,'fsMplsRsvpTeReoptimizeTime':fsMplsRsvpTeReoptimizeTime,'fsMplsRsvpTeEroCacheTime':fsMplsRsvpTeEroCacheTime,'fsMplsRsvpTeReoptLinkMaintenance':fsMplsRsvpTeReoptLinkMaintenance,'fsMplsRsvpTeReoptNodeMaintenance':fsMplsRsvpTeReoptNodeMaintenance})