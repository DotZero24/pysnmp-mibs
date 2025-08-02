_w='ospfVirtNbrRtrId'
_v='ospfVirtNbrArea'
_u='loading'
_t='exchange'
_s='exchangeStart'
_r='twoWay'
_q='attempt'
_p='RouterID'
_o='ospfNbrAddressLessIndex'
_n='ospfNbrIpAddr'
_m='ospfVirtIfNeighbor'
_l='ospfVirtIfAreaID'
_k='ospfIfMetricTOS'
_j='ospfIfMetricAddressLessIf'
_i='ospfIfMetricIpAddress'
_h='0000000000000000'
_g='Status'
_f='AreaID'
_e='ospfAddressLessIf'
_d='ospfIfIpAddress'
_c='ospfHostTOS'
_b='ospfHostIpAddress'
_a='ospfAreaRangeNet'
_Z='ospfAreaRangeAreaID'
_Y='ospfLsdbRouterId'
_X='ospfLsdbLSID'
_W='ospfLsdbType'
_V='ospfLsdbAreaId'
_U='ospfStubTOS'
_T='ospfStubAreaID'
_S='TruthValue'
_R='ospfAreaId'
_Q='HelloRange'
_P='DesignatedRouterPriority'
_O='pointToPoint'
_N='IpAddress'
_M='OctetString'
_L='down'
_K='PositiveInteger'
_J='00000000'
_I='UpToMaxAge'
_H='Gauge32'
_G='Counter32'
_F='Validation'
_E='Integer32'
_D='RFC1253-MIB'
_C='read-only'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_M,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits',_G,'Counter64',_H,_E,_N,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class AreaID(IpAddress):0
class RouterID(IpAddress):0
class Metric(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
class BigMetric(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16777215))
class TruthValue(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
class Status(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
class Validation(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),('invalid',2)))
class PositiveInteger(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
class HelloRange(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
class UpToMaxAge(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3600))
class InterfaceIndex(Integer32):0
class DesignatedRouterPriority(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
class TOSType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_Ospf_ObjectIdentity=ObjectIdentity
ospf=_Ospf_ObjectIdentity((1,3,6,1,2,1,14))
_OspfGeneralGroup_ObjectIdentity=ObjectIdentity
ospfGeneralGroup=_OspfGeneralGroup_ObjectIdentity((1,3,6,1,2,1,14,1))
_OspfRouterId_Type=RouterID
_OspfRouterId_Object=MibScalar
ospfRouterId=_OspfRouterId_Object((1,3,6,1,2,1,14,1,1),_OspfRouterId_Type())
ospfRouterId.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfRouterId.setStatus(_A)
_OspfAdminStat_Type=Status
_OspfAdminStat_Object=MibScalar
ospfAdminStat=_OspfAdminStat_Object((1,3,6,1,2,1,14,1,2),_OspfAdminStat_Type())
ospfAdminStat.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAdminStat.setStatus(_A)
class _OspfVersionNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(2));namedValues=NamedValues(('version2',2))
_OspfVersionNumber_Type.__name__=_E
_OspfVersionNumber_Object=MibScalar
ospfVersionNumber=_OspfVersionNumber_Object((1,3,6,1,2,1,14,1,3),_OspfVersionNumber_Type())
ospfVersionNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:ospfVersionNumber.setStatus(_A)
_OspfAreaBdrRtrStatus_Type=TruthValue
_OspfAreaBdrRtrStatus_Object=MibScalar
ospfAreaBdrRtrStatus=_OspfAreaBdrRtrStatus_Object((1,3,6,1,2,1,14,1,4),_OspfAreaBdrRtrStatus_Type())
ospfAreaBdrRtrStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ospfAreaBdrRtrStatus.setStatus(_A)
_OspfASBdrRtrStatus_Type=TruthValue
_OspfASBdrRtrStatus_Object=MibScalar
ospfASBdrRtrStatus=_OspfASBdrRtrStatus_Object((1,3,6,1,2,1,14,1,5),_OspfASBdrRtrStatus_Type())
ospfASBdrRtrStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfASBdrRtrStatus.setStatus(_A)
_OspfExternLSACount_Type=Gauge32
_OspfExternLSACount_Object=MibScalar
ospfExternLSACount=_OspfExternLSACount_Object((1,3,6,1,2,1,14,1,6),_OspfExternLSACount_Type())
ospfExternLSACount.setMaxAccess(_C)
if mibBuilder.loadTexts:ospfExternLSACount.setStatus(_A)
_OspfExternLSACksumSum_Type=Integer32
_OspfExternLSACksumSum_Object=MibScalar
ospfExternLSACksumSum=_OspfExternLSACksumSum_Object((1,3,6,1,2,1,14,1,7),_OspfExternLSACksumSum_Type())
ospfExternLSACksumSum.setMaxAccess(_C)
if mibBuilder.loadTexts:ospfExternLSACksumSum.setStatus(_A)
_OspfTOSSupport_Type=TruthValue
_OspfTOSSupport_Object=MibScalar
ospfTOSSupport=_OspfTOSSupport_Object((1,3,6,1,2,1,14,1,8),_OspfTOSSupport_Type())
ospfTOSSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfTOSSupport.setStatus(_A)
_OspfOriginateNewLSAs_Type=Counter32
_OspfOriginateNewLSAs_Object=MibScalar
ospfOriginateNewLSAs=_OspfOriginateNewLSAs_Object((1,3,6,1,2,1,14,1,9),_OspfOriginateNewLSAs_Type())
ospfOriginateNewLSAs.setMaxAccess(_C)
if mibBuilder.loadTexts:ospfOriginateNewLSAs.setStatus(_A)
_OspfRxNewLSAs_Type=Counter32
_OspfRxNewLSAs_Object=MibScalar
ospfRxNewLSAs=_OspfRxNewLSAs_Object((1,3,6,1,2,1,14,1,10),_OspfRxNewLSAs_Type())
ospfRxNewLSAs.setMaxAccess(_C)
if mibBuilder.loadTexts:ospfRxNewLSAs.setStatus(_A)
_OspfAreaTable_Object=MibTable
ospfAreaTable=_OspfAreaTable_Object((1,3,6,1,2,1,14,2))
if mibBuilder.loadTexts:ospfAreaTable.setStatus(_A)
_OspfAreaEntry_Object=MibTableRow
ospfAreaEntry=_OspfAreaEntry_Object((1,3,6,1,2,1,14,2,1))
ospfAreaEntry.setIndexNames((0,_D,_R))
if mibBuilder.loadTexts:ospfAreaEntry.setStatus(_A)
_OspfAreaId_Type=AreaID
_OspfAreaId_Object=MibTableColumn
ospfAreaId=_OspfAreaId_Object((1,3,6,1,2,1,14,2,1,1),_OspfAreaId_Type())
ospfAreaId.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaId.setStatus(_A)
class _OspfAuthType_Type(Integer32):defaultValue=0
_OspfAuthType_Type.__name__=_E
_OspfAuthType_Object=MibTableColumn
ospfAuthType=_OspfAuthType_Object((1,3,6,1,2,1,14,2,1,2),_OspfAuthType_Type())
ospfAuthType.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAuthType.setStatus(_A)
class _OspfImportASExtern_Type(TruthValue):defaultValue=1
_OspfImportASExtern_Type.__name__=_S
_OspfImportASExtern_Object=MibTableColumn
ospfImportASExtern=_OspfImportASExtern_Object((1,3,6,1,2,1,14,2,1,3),_OspfImportASExtern_Type())
ospfImportASExtern.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfImportASExtern.setStatus(_A)
class _OspfSpfRuns_Type(Counter32):defaultValue=0
_OspfSpfRuns_Type.__name__=_G
_OspfSpfRuns_Object=MibTableColumn
ospfSpfRuns=_OspfSpfRuns_Object((1,3,6,1,2,1,14,2,1,4),_OspfSpfRuns_Type())
ospfSpfRuns.setMaxAccess(_C)
if mibBuilder.loadTexts:ospfSpfRuns.setStatus(_A)
class _OspfAreaBdrRtrCount_Type(Gauge32):defaultValue=0
_OspfAreaBdrRtrCount_Type.__name__=_H
_OspfAreaBdrRtrCount_Object=MibTableColumn
ospfAreaBdrRtrCount=_OspfAreaBdrRtrCount_Object((1,3,6,1,2,1,14,2,1,5),_OspfAreaBdrRtrCount_Type())
ospfAreaBdrRtrCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ospfAreaBdrRtrCount.setStatus(_A)
class _OspfASBdrRtrCount_Type(Gauge32):defaultValue=0
_OspfASBdrRtrCount_Type.__name__=_H
_OspfASBdrRtrCount_Object=MibTableColumn
ospfASBdrRtrCount=_OspfASBdrRtrCount_Object((1,3,6,1,2,1,14,2,1,6),_OspfASBdrRtrCount_Type())
ospfASBdrRtrCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ospfASBdrRtrCount.setStatus(_A)
class _OspfAreaLSACount_Type(Gauge32):defaultValue=0
_OspfAreaLSACount_Type.__name__=_H
_OspfAreaLSACount_Object=MibTableColumn
ospfAreaLSACount=_OspfAreaLSACount_Object((1,3,6,1,2,1,14,2,1,7),_OspfAreaLSACount_Type())
ospfAreaLSACount.setMaxAccess(_C)
if mibBuilder.loadTexts:ospfAreaLSACount.setStatus(_A)
class _OspfAreaLSACksumSum_Type(Integer32):defaultValue=0
_OspfAreaLSACksumSum_Type.__name__=_E
_OspfAreaLSACksumSum_Object=MibTableColumn
ospfAreaLSACksumSum=_OspfAreaLSACksumSum_Object((1,3,6,1,2,1,14,2,1,8),_OspfAreaLSACksumSum_Type())
ospfAreaLSACksumSum.setMaxAccess(_C)
if mibBuilder.loadTexts:ospfAreaLSACksumSum.setStatus(_A)
_OspfStubAreaTable_Object=MibTable
ospfStubAreaTable=_OspfStubAreaTable_Object((1,3,6,1,2,1,14,3))
if mibBuilder.loadTexts:ospfStubAreaTable.setStatus(_A)
_OspfStubAreaEntry_Object=MibTableRow
ospfStubAreaEntry=_OspfStubAreaEntry_Object((1,3,6,1,2,1,14,3,1))
ospfStubAreaEntry.setIndexNames((0,_D,_T),(0,_D,_U))
if mibBuilder.loadTexts:ospfStubAreaEntry.setStatus(_A)
_OspfStubAreaID_Type=AreaID
_OspfStubAreaID_Object=MibTableColumn
ospfStubAreaID=_OspfStubAreaID_Object((1,3,6,1,2,1,14,3,1,1),_OspfStubAreaID_Type())
ospfStubAreaID.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfStubAreaID.setStatus(_A)
_OspfStubTOS_Type=TOSType
_OspfStubTOS_Object=MibTableColumn
ospfStubTOS=_OspfStubTOS_Object((1,3,6,1,2,1,14,3,1,2),_OspfStubTOS_Type())
ospfStubTOS.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfStubTOS.setStatus(_A)
_OspfStubMetric_Type=BigMetric
_OspfStubMetric_Object=MibTableColumn
ospfStubMetric=_OspfStubMetric_Object((1,3,6,1,2,1,14,3,1,3),_OspfStubMetric_Type())
ospfStubMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfStubMetric.setStatus(_A)
class _OspfStubStatus_Type(Validation):defaultValue=1
_OspfStubStatus_Type.__name__=_F
_OspfStubStatus_Object=MibTableColumn
ospfStubStatus=_OspfStubStatus_Object((1,3,6,1,2,1,14,3,1,4),_OspfStubStatus_Type())
ospfStubStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfStubStatus.setStatus(_A)
_OspfLsdbTable_Object=MibTable
ospfLsdbTable=_OspfLsdbTable_Object((1,3,6,1,2,1,14,4))
if mibBuilder.loadTexts:ospfLsdbTable.setStatus(_A)
_OspfLsdbEntry_Object=MibTableRow
ospfLsdbEntry=_OspfLsdbEntry_Object((1,3,6,1,2,1,14,4,1))
ospfLsdbEntry.setIndexNames((0,_D,_V),(0,_D,_W),(0,_D,_X),(0,_D,_Y))
if mibBuilder.loadTexts:ospfLsdbEntry.setStatus(_A)
_OspfLsdbAreaId_Type=AreaID
_OspfLsdbAreaId_Object=MibTableColumn
ospfLsdbAreaId=_OspfLsdbAreaId_Object((1,3,6,1,2,1,14,4,1,1),_OspfLsdbAreaId_Type())
ospfLsdbAreaId.setMaxAccess(_C)
if mibBuilder.loadTexts:ospfLsdbAreaId.setStatus(_A)
class _OspfLsdbType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('routerLink',1),('networkLink',2),('summaryLink',3),('asSummaryLink',4),('asExternalLink',5)))
_OspfLsdbType_Type.__name__=_E
_OspfLsdbType_Object=MibTableColumn
ospfLsdbType=_OspfLsdbType_Object((1,3,6,1,2,1,14,4,1,2),_OspfLsdbType_Type())
ospfLsdbType.setMaxAccess(_C)
if mibBuilder.loadTexts:ospfLsdbType.setStatus(_A)
_OspfLsdbLSID_Type=IpAddress
_OspfLsdbLSID_Object=MibTableColumn
ospfLsdbLSID=_OspfLsdbLSID_Object((1,3,6,1,2,1,14,4,1,3),_OspfLsdbLSID_Type())
ospfLsdbLSID.setMaxAccess(_C)
if mibBuilder.loadTexts:ospfLsdbLSID.setStatus(_A)
_OspfLsdbRouterId_Type=RouterID
_OspfLsdbRouterId_Object=MibTableColumn
ospfLsdbRouterId=_OspfLsdbRouterId_Object((1,3,6,1,2,1,14,4,1,4),_OspfLsdbRouterId_Type())
ospfLsdbRouterId.setMaxAccess(_C)
if mibBuilder.loadTexts:ospfLsdbRouterId.setStatus(_A)
_OspfLsdbSequence_Type=Integer32
_OspfLsdbSequence_Object=MibTableColumn
ospfLsdbSequence=_OspfLsdbSequence_Object((1,3,6,1,2,1,14,4,1,5),_OspfLsdbSequence_Type())
ospfLsdbSequence.setMaxAccess(_C)
if mibBuilder.loadTexts:ospfLsdbSequence.setStatus(_A)
_OspfLsdbAge_Type=Integer32
_OspfLsdbAge_Object=MibTableColumn
ospfLsdbAge=_OspfLsdbAge_Object((1,3,6,1,2,1,14,4,1,6),_OspfLsdbAge_Type())
ospfLsdbAge.setMaxAccess(_C)
if mibBuilder.loadTexts:ospfLsdbAge.setStatus(_A)
_OspfLsdbChecksum_Type=Integer32
_OspfLsdbChecksum_Object=MibTableColumn
ospfLsdbChecksum=_OspfLsdbChecksum_Object((1,3,6,1,2,1,14,4,1,7),_OspfLsdbChecksum_Type())
ospfLsdbChecksum.setMaxAccess(_C)
if mibBuilder.loadTexts:ospfLsdbChecksum.setStatus(_A)
_OspfLsdbAdvertisement_Type=OctetString
_OspfLsdbAdvertisement_Object=MibTableColumn
ospfLsdbAdvertisement=_OspfLsdbAdvertisement_Object((1,3,6,1,2,1,14,4,1,8),_OspfLsdbAdvertisement_Type())
ospfLsdbAdvertisement.setMaxAccess(_C)
if mibBuilder.loadTexts:ospfLsdbAdvertisement.setStatus(_A)
_OspfAreaRangeTable_Object=MibTable
ospfAreaRangeTable=_OspfAreaRangeTable_Object((1,3,6,1,2,1,14,5))
if mibBuilder.loadTexts:ospfAreaRangeTable.setStatus(_A)
_OspfAreaRangeEntry_Object=MibTableRow
ospfAreaRangeEntry=_OspfAreaRangeEntry_Object((1,3,6,1,2,1,14,5,1))
ospfAreaRangeEntry.setIndexNames((0,_D,_Z),(0,_D,_a))
if mibBuilder.loadTexts:ospfAreaRangeEntry.setStatus(_A)
_OspfAreaRangeAreaID_Type=AreaID
_OspfAreaRangeAreaID_Object=MibTableColumn
ospfAreaRangeAreaID=_OspfAreaRangeAreaID_Object((1,3,6,1,2,1,14,5,1,1),_OspfAreaRangeAreaID_Type())
ospfAreaRangeAreaID.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaRangeAreaID.setStatus(_A)
_OspfAreaRangeNet_Type=IpAddress
_OspfAreaRangeNet_Object=MibTableColumn
ospfAreaRangeNet=_OspfAreaRangeNet_Object((1,3,6,1,2,1,14,5,1,2),_OspfAreaRangeNet_Type())
ospfAreaRangeNet.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaRangeNet.setStatus(_A)
_OspfAreaRangeMask_Type=IpAddress
_OspfAreaRangeMask_Object=MibTableColumn
ospfAreaRangeMask=_OspfAreaRangeMask_Object((1,3,6,1,2,1,14,5,1,3),_OspfAreaRangeMask_Type())
ospfAreaRangeMask.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaRangeMask.setStatus(_A)
class _OspfAreaRangeStatus_Type(Validation):defaultValue=1
_OspfAreaRangeStatus_Type.__name__=_F
_OspfAreaRangeStatus_Object=MibTableColumn
ospfAreaRangeStatus=_OspfAreaRangeStatus_Object((1,3,6,1,2,1,14,5,1,4),_OspfAreaRangeStatus_Type())
ospfAreaRangeStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAreaRangeStatus.setStatus(_A)
_OspfHostTable_Object=MibTable
ospfHostTable=_OspfHostTable_Object((1,3,6,1,2,1,14,6))
if mibBuilder.loadTexts:ospfHostTable.setStatus(_A)
_OspfHostEntry_Object=MibTableRow
ospfHostEntry=_OspfHostEntry_Object((1,3,6,1,2,1,14,6,1))
ospfHostEntry.setIndexNames((0,_D,_b),(0,_D,_c))
if mibBuilder.loadTexts:ospfHostEntry.setStatus(_A)
_OspfHostIpAddress_Type=IpAddress
_OspfHostIpAddress_Object=MibTableColumn
ospfHostIpAddress=_OspfHostIpAddress_Object((1,3,6,1,2,1,14,6,1,1),_OspfHostIpAddress_Type())
ospfHostIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfHostIpAddress.setStatus(_A)
_OspfHostTOS_Type=TOSType
_OspfHostTOS_Object=MibTableColumn
ospfHostTOS=_OspfHostTOS_Object((1,3,6,1,2,1,14,6,1,2),_OspfHostTOS_Type())
ospfHostTOS.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfHostTOS.setStatus(_A)
_OspfHostMetric_Type=Metric
_OspfHostMetric_Object=MibTableColumn
ospfHostMetric=_OspfHostMetric_Object((1,3,6,1,2,1,14,6,1,3),_OspfHostMetric_Type())
ospfHostMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfHostMetric.setStatus(_A)
class _OspfHostStatus_Type(Validation):defaultValue=1
_OspfHostStatus_Type.__name__=_F
_OspfHostStatus_Object=MibTableColumn
ospfHostStatus=_OspfHostStatus_Object((1,3,6,1,2,1,14,6,1,4),_OspfHostStatus_Type())
ospfHostStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfHostStatus.setStatus(_A)
_OspfIfTable_Object=MibTable
ospfIfTable=_OspfIfTable_Object((1,3,6,1,2,1,14,7))
if mibBuilder.loadTexts:ospfIfTable.setStatus(_A)
_OspfIfEntry_Object=MibTableRow
ospfIfEntry=_OspfIfEntry_Object((1,3,6,1,2,1,14,7,1))
ospfIfEntry.setIndexNames((0,_D,_d),(0,_D,_e))
if mibBuilder.loadTexts:ospfIfEntry.setStatus(_A)
_OspfIfIpAddress_Type=IpAddress
_OspfIfIpAddress_Object=MibTableColumn
ospfIfIpAddress=_OspfIfIpAddress_Object((1,3,6,1,2,1,14,7,1,1),_OspfIfIpAddress_Type())
ospfIfIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIfIpAddress.setStatus(_A)
_OspfAddressLessIf_Type=Integer32
_OspfAddressLessIf_Object=MibTableColumn
ospfAddressLessIf=_OspfAddressLessIf_Object((1,3,6,1,2,1,14,7,1,2),_OspfAddressLessIf_Type())
ospfAddressLessIf.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfAddressLessIf.setStatus(_A)
class _OspfIfAreaId_Type(AreaID):defaultHexValue=_J
_OspfIfAreaId_Type.__name__=_f
_OspfIfAreaId_Object=MibTableColumn
ospfIfAreaId=_OspfIfAreaId_Object((1,3,6,1,2,1,14,7,1,3),_OspfIfAreaId_Type())
ospfIfAreaId.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIfAreaId.setStatus(_A)
class _OspfIfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('broadcast',1),('nbma',2),(_O,3)))
_OspfIfType_Type.__name__=_E
_OspfIfType_Object=MibTableColumn
ospfIfType=_OspfIfType_Object((1,3,6,1,2,1,14,7,1,4),_OspfIfType_Type())
ospfIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIfType.setStatus(_A)
class _OspfIfAdminStat_Type(Status):defaultValue=1
_OspfIfAdminStat_Type.__name__=_g
_OspfIfAdminStat_Object=MibTableColumn
ospfIfAdminStat=_OspfIfAdminStat_Object((1,3,6,1,2,1,14,7,1,5),_OspfIfAdminStat_Type())
ospfIfAdminStat.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIfAdminStat.setStatus(_A)
class _OspfIfRtrPriority_Type(DesignatedRouterPriority):defaultValue=1
_OspfIfRtrPriority_Type.__name__=_P
_OspfIfRtrPriority_Object=MibTableColumn
ospfIfRtrPriority=_OspfIfRtrPriority_Object((1,3,6,1,2,1,14,7,1,6),_OspfIfRtrPriority_Type())
ospfIfRtrPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIfRtrPriority.setStatus(_A)
class _OspfIfTransitDelay_Type(UpToMaxAge):defaultValue=1
_OspfIfTransitDelay_Type.__name__=_I
_OspfIfTransitDelay_Object=MibTableColumn
ospfIfTransitDelay=_OspfIfTransitDelay_Object((1,3,6,1,2,1,14,7,1,7),_OspfIfTransitDelay_Type())
ospfIfTransitDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIfTransitDelay.setStatus(_A)
class _OspfIfRetransInterval_Type(UpToMaxAge):defaultValue=5
_OspfIfRetransInterval_Type.__name__=_I
_OspfIfRetransInterval_Object=MibTableColumn
ospfIfRetransInterval=_OspfIfRetransInterval_Object((1,3,6,1,2,1,14,7,1,8),_OspfIfRetransInterval_Type())
ospfIfRetransInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIfRetransInterval.setStatus(_A)
class _OspfIfHelloInterval_Type(HelloRange):defaultValue=10
_OspfIfHelloInterval_Type.__name__=_Q
_OspfIfHelloInterval_Object=MibTableColumn
ospfIfHelloInterval=_OspfIfHelloInterval_Object((1,3,6,1,2,1,14,7,1,9),_OspfIfHelloInterval_Type())
ospfIfHelloInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIfHelloInterval.setStatus(_A)
class _OspfIfRtrDeadInterval_Type(PositiveInteger):defaultValue=40
_OspfIfRtrDeadInterval_Type.__name__=_K
_OspfIfRtrDeadInterval_Object=MibTableColumn
ospfIfRtrDeadInterval=_OspfIfRtrDeadInterval_Object((1,3,6,1,2,1,14,7,1,10),_OspfIfRtrDeadInterval_Type())
ospfIfRtrDeadInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIfRtrDeadInterval.setStatus(_A)
class _OspfIfPollInterval_Type(PositiveInteger):defaultValue=120
_OspfIfPollInterval_Type.__name__=_K
_OspfIfPollInterval_Object=MibTableColumn
ospfIfPollInterval=_OspfIfPollInterval_Object((1,3,6,1,2,1,14,7,1,11),_OspfIfPollInterval_Type())
ospfIfPollInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIfPollInterval.setStatus(_A)
class _OspfIfState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_L,1),('loopback',2),('waiting',3),(_O,4),('designatedRouter',5),('backupDesignatedRouter',6),('otherDesignatedRouter',7)))
_OspfIfState_Type.__name__=_E
_OspfIfState_Object=MibTableColumn
ospfIfState=_OspfIfState_Object((1,3,6,1,2,1,14,7,1,12),_OspfIfState_Type())
ospfIfState.setMaxAccess(_C)
if mibBuilder.loadTexts:ospfIfState.setStatus(_A)
class _OspfIfDesignatedRouter_Type(IpAddress):defaultHexValue=_J
_OspfIfDesignatedRouter_Type.__name__=_N
_OspfIfDesignatedRouter_Object=MibTableColumn
ospfIfDesignatedRouter=_OspfIfDesignatedRouter_Object((1,3,6,1,2,1,14,7,1,13),_OspfIfDesignatedRouter_Type())
ospfIfDesignatedRouter.setMaxAccess(_C)
if mibBuilder.loadTexts:ospfIfDesignatedRouter.setStatus(_A)
class _OspfIfBackupDesignatedRouter_Type(IpAddress):defaultHexValue=_J
_OspfIfBackupDesignatedRouter_Type.__name__=_N
_OspfIfBackupDesignatedRouter_Object=MibTableColumn
ospfIfBackupDesignatedRouter=_OspfIfBackupDesignatedRouter_Object((1,3,6,1,2,1,14,7,1,14),_OspfIfBackupDesignatedRouter_Type())
ospfIfBackupDesignatedRouter.setMaxAccess(_C)
if mibBuilder.loadTexts:ospfIfBackupDesignatedRouter.setStatus(_A)
class _OspfIfEvents_Type(Counter32):defaultValue=0
_OspfIfEvents_Type.__name__=_G
_OspfIfEvents_Object=MibTableColumn
ospfIfEvents=_OspfIfEvents_Object((1,3,6,1,2,1,14,7,1,15),_OspfIfEvents_Type())
ospfIfEvents.setMaxAccess(_C)
if mibBuilder.loadTexts:ospfIfEvents.setStatus(_A)
class _OspfIfAuthKey_Type(OctetString):defaultHexValue=_h
_OspfIfAuthKey_Type.__name__=_M
_OspfIfAuthKey_Object=MibTableColumn
ospfIfAuthKey=_OspfIfAuthKey_Object((1,3,6,1,2,1,14,7,1,16),_OspfIfAuthKey_Type())
ospfIfAuthKey.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIfAuthKey.setStatus(_A)
_OspfIfMetricTable_Object=MibTable
ospfIfMetricTable=_OspfIfMetricTable_Object((1,3,6,1,2,1,14,8))
if mibBuilder.loadTexts:ospfIfMetricTable.setStatus(_A)
_OspfIfMetricEntry_Object=MibTableRow
ospfIfMetricEntry=_OspfIfMetricEntry_Object((1,3,6,1,2,1,14,8,1))
ospfIfMetricEntry.setIndexNames((0,_D,_i),(0,_D,_j),(0,_D,_k))
if mibBuilder.loadTexts:ospfIfMetricEntry.setStatus(_A)
_OspfIfMetricIpAddress_Type=IpAddress
_OspfIfMetricIpAddress_Object=MibTableColumn
ospfIfMetricIpAddress=_OspfIfMetricIpAddress_Object((1,3,6,1,2,1,14,8,1,1),_OspfIfMetricIpAddress_Type())
ospfIfMetricIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIfMetricIpAddress.setStatus(_A)
_OspfIfMetricAddressLessIf_Type=Integer32
_OspfIfMetricAddressLessIf_Object=MibTableColumn
ospfIfMetricAddressLessIf=_OspfIfMetricAddressLessIf_Object((1,3,6,1,2,1,14,8,1,2),_OspfIfMetricAddressLessIf_Type())
ospfIfMetricAddressLessIf.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIfMetricAddressLessIf.setStatus(_A)
_OspfIfMetricTOS_Type=TOSType
_OspfIfMetricTOS_Object=MibTableColumn
ospfIfMetricTOS=_OspfIfMetricTOS_Object((1,3,6,1,2,1,14,8,1,3),_OspfIfMetricTOS_Type())
ospfIfMetricTOS.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIfMetricTOS.setStatus(_A)
_OspfIfMetricMetric_Type=Metric
_OspfIfMetricMetric_Object=MibTableColumn
ospfIfMetricMetric=_OspfIfMetricMetric_Object((1,3,6,1,2,1,14,8,1,4),_OspfIfMetricMetric_Type())
ospfIfMetricMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIfMetricMetric.setStatus(_A)
class _OspfIfMetricStatus_Type(Validation):defaultValue=1
_OspfIfMetricStatus_Type.__name__=_F
_OspfIfMetricStatus_Object=MibTableColumn
ospfIfMetricStatus=_OspfIfMetricStatus_Object((1,3,6,1,2,1,14,8,1,5),_OspfIfMetricStatus_Type())
ospfIfMetricStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfIfMetricStatus.setStatus(_A)
_OspfVirtIfTable_Object=MibTable
ospfVirtIfTable=_OspfVirtIfTable_Object((1,3,6,1,2,1,14,9))
if mibBuilder.loadTexts:ospfVirtIfTable.setStatus(_A)
_OspfVirtIfEntry_Object=MibTableRow
ospfVirtIfEntry=_OspfVirtIfEntry_Object((1,3,6,1,2,1,14,9,1))
ospfVirtIfEntry.setIndexNames((0,_D,_l),(0,_D,_m))
if mibBuilder.loadTexts:ospfVirtIfEntry.setStatus(_A)
_OspfVirtIfAreaID_Type=AreaID
_OspfVirtIfAreaID_Object=MibTableColumn
ospfVirtIfAreaID=_OspfVirtIfAreaID_Object((1,3,6,1,2,1,14,9,1,1),_OspfVirtIfAreaID_Type())
ospfVirtIfAreaID.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfVirtIfAreaID.setStatus(_A)
_OspfVirtIfNeighbor_Type=RouterID
_OspfVirtIfNeighbor_Object=MibTableColumn
ospfVirtIfNeighbor=_OspfVirtIfNeighbor_Object((1,3,6,1,2,1,14,9,1,2),_OspfVirtIfNeighbor_Type())
ospfVirtIfNeighbor.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfVirtIfNeighbor.setStatus(_A)
class _OspfVirtIfTransitDelay_Type(UpToMaxAge):defaultValue=1
_OspfVirtIfTransitDelay_Type.__name__=_I
_OspfVirtIfTransitDelay_Object=MibTableColumn
ospfVirtIfTransitDelay=_OspfVirtIfTransitDelay_Object((1,3,6,1,2,1,14,9,1,3),_OspfVirtIfTransitDelay_Type())
ospfVirtIfTransitDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfVirtIfTransitDelay.setStatus(_A)
class _OspfVirtIfRetransInterval_Type(UpToMaxAge):defaultValue=5
_OspfVirtIfRetransInterval_Type.__name__=_I
_OspfVirtIfRetransInterval_Object=MibTableColumn
ospfVirtIfRetransInterval=_OspfVirtIfRetransInterval_Object((1,3,6,1,2,1,14,9,1,4),_OspfVirtIfRetransInterval_Type())
ospfVirtIfRetransInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfVirtIfRetransInterval.setStatus(_A)
class _OspfVirtIfHelloInterval_Type(HelloRange):defaultValue=10
_OspfVirtIfHelloInterval_Type.__name__=_Q
_OspfVirtIfHelloInterval_Object=MibTableColumn
ospfVirtIfHelloInterval=_OspfVirtIfHelloInterval_Object((1,3,6,1,2,1,14,9,1,5),_OspfVirtIfHelloInterval_Type())
ospfVirtIfHelloInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfVirtIfHelloInterval.setStatus(_A)
class _OspfVirtIfRtrDeadInterval_Type(PositiveInteger):defaultValue=60
_OspfVirtIfRtrDeadInterval_Type.__name__=_K
_OspfVirtIfRtrDeadInterval_Object=MibTableColumn
ospfVirtIfRtrDeadInterval=_OspfVirtIfRtrDeadInterval_Object((1,3,6,1,2,1,14,9,1,6),_OspfVirtIfRtrDeadInterval_Type())
ospfVirtIfRtrDeadInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfVirtIfRtrDeadInterval.setStatus(_A)
class _OspfVirtIfState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4)));namedValues=NamedValues(*((_L,1),(_O,4)))
_OspfVirtIfState_Type.__name__=_E
_OspfVirtIfState_Object=MibTableColumn
ospfVirtIfState=_OspfVirtIfState_Object((1,3,6,1,2,1,14,9,1,7),_OspfVirtIfState_Type())
ospfVirtIfState.setMaxAccess(_C)
if mibBuilder.loadTexts:ospfVirtIfState.setStatus(_A)
class _OspfVirtIfEvents_Type(Counter32):defaultValue=0
_OspfVirtIfEvents_Type.__name__=_G
_OspfVirtIfEvents_Object=MibTableColumn
ospfVirtIfEvents=_OspfVirtIfEvents_Object((1,3,6,1,2,1,14,9,1,8),_OspfVirtIfEvents_Type())
ospfVirtIfEvents.setMaxAccess(_C)
if mibBuilder.loadTexts:ospfVirtIfEvents.setStatus(_A)
class _OspfVirtIfAuthKey_Type(OctetString):defaultHexValue=_h
_OspfVirtIfAuthKey_Type.__name__=_M
_OspfVirtIfAuthKey_Object=MibTableColumn
ospfVirtIfAuthKey=_OspfVirtIfAuthKey_Object((1,3,6,1,2,1,14,9,1,9),_OspfVirtIfAuthKey_Type())
ospfVirtIfAuthKey.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfVirtIfAuthKey.setStatus(_A)
class _OspfVirtIfStatus_Type(Validation):defaultValue=1
_OspfVirtIfStatus_Type.__name__=_F
_OspfVirtIfStatus_Object=MibTableColumn
ospfVirtIfStatus=_OspfVirtIfStatus_Object((1,3,6,1,2,1,14,9,1,10),_OspfVirtIfStatus_Type())
ospfVirtIfStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfVirtIfStatus.setStatus(_A)
_OspfNbrTable_Object=MibTable
ospfNbrTable=_OspfNbrTable_Object((1,3,6,1,2,1,14,10))
if mibBuilder.loadTexts:ospfNbrTable.setStatus(_A)
_OspfNbrEntry_Object=MibTableRow
ospfNbrEntry=_OspfNbrEntry_Object((1,3,6,1,2,1,14,10,1))
ospfNbrEntry.setIndexNames((0,_D,_n),(0,_D,_o))
if mibBuilder.loadTexts:ospfNbrEntry.setStatus(_A)
_OspfNbrIpAddr_Type=IpAddress
_OspfNbrIpAddr_Object=MibTableColumn
ospfNbrIpAddr=_OspfNbrIpAddr_Object((1,3,6,1,2,1,14,10,1,1),_OspfNbrIpAddr_Type())
ospfNbrIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfNbrIpAddr.setStatus(_A)
_OspfNbrAddressLessIndex_Type=InterfaceIndex
_OspfNbrAddressLessIndex_Object=MibTableColumn
ospfNbrAddressLessIndex=_OspfNbrAddressLessIndex_Object((1,3,6,1,2,1,14,10,1,2),_OspfNbrAddressLessIndex_Type())
ospfNbrAddressLessIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfNbrAddressLessIndex.setStatus(_A)
class _OspfNbrRtrId_Type(RouterID):defaultHexValue=_J
_OspfNbrRtrId_Type.__name__=_p
_OspfNbrRtrId_Object=MibTableColumn
ospfNbrRtrId=_OspfNbrRtrId_Object((1,3,6,1,2,1,14,10,1,3),_OspfNbrRtrId_Type())
ospfNbrRtrId.setMaxAccess(_C)
if mibBuilder.loadTexts:ospfNbrRtrId.setStatus(_A)
class _OspfNbrOptions_Type(Integer32):defaultValue=0
_OspfNbrOptions_Type.__name__=_E
_OspfNbrOptions_Object=MibTableColumn
ospfNbrOptions=_OspfNbrOptions_Object((1,3,6,1,2,1,14,10,1,4),_OspfNbrOptions_Type())
ospfNbrOptions.setMaxAccess(_C)
if mibBuilder.loadTexts:ospfNbrOptions.setStatus(_A)
class _OspfNbrPriority_Type(DesignatedRouterPriority):defaultValue=1
_OspfNbrPriority_Type.__name__=_P
_OspfNbrPriority_Object=MibTableColumn
ospfNbrPriority=_OspfNbrPriority_Object((1,3,6,1,2,1,14,10,1,5),_OspfNbrPriority_Type())
ospfNbrPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfNbrPriority.setStatus(_A)
class _OspfNbrState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_L,1),(_q,2),('init',3),(_r,4),(_s,5),(_t,6),(_u,7),('full',8)))
_OspfNbrState_Type.__name__=_E
_OspfNbrState_Object=MibTableColumn
ospfNbrState=_OspfNbrState_Object((1,3,6,1,2,1,14,10,1,6),_OspfNbrState_Type())
ospfNbrState.setMaxAccess(_C)
if mibBuilder.loadTexts:ospfNbrState.setStatus(_A)
class _OspfNbrEvents_Type(Counter32):defaultValue=0
_OspfNbrEvents_Type.__name__=_G
_OspfNbrEvents_Object=MibTableColumn
ospfNbrEvents=_OspfNbrEvents_Object((1,3,6,1,2,1,14,10,1,7),_OspfNbrEvents_Type())
ospfNbrEvents.setMaxAccess(_C)
if mibBuilder.loadTexts:ospfNbrEvents.setStatus(_A)
class _OspfNbrLSRetransQLen_Type(Gauge32):defaultValue=0
_OspfNbrLSRetransQLen_Type.__name__=_H
_OspfNbrLSRetransQLen_Object=MibTableColumn
ospfNbrLSRetransQLen=_OspfNbrLSRetransQLen_Object((1,3,6,1,2,1,14,10,1,8),_OspfNbrLSRetransQLen_Type())
ospfNbrLSRetransQLen.setMaxAccess(_C)
if mibBuilder.loadTexts:ospfNbrLSRetransQLen.setStatus(_A)
class _OspfNBMANbrStatus_Type(Validation):defaultValue=1
_OspfNBMANbrStatus_Type.__name__=_F
_OspfNBMANbrStatus_Object=MibTableColumn
ospfNBMANbrStatus=_OspfNBMANbrStatus_Object((1,3,6,1,2,1,14,10,1,9),_OspfNBMANbrStatus_Type())
ospfNBMANbrStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ospfNBMANbrStatus.setStatus(_A)
_OspfVirtNbrTable_Object=MibTable
ospfVirtNbrTable=_OspfVirtNbrTable_Object((1,3,6,1,2,1,14,11))
if mibBuilder.loadTexts:ospfVirtNbrTable.setStatus(_A)
_OspfVirtNbrEntry_Object=MibTableRow
ospfVirtNbrEntry=_OspfVirtNbrEntry_Object((1,3,6,1,2,1,14,11,1))
ospfVirtNbrEntry.setIndexNames((0,_D,_v),(0,_D,_w))
if mibBuilder.loadTexts:ospfVirtNbrEntry.setStatus(_A)
_OspfVirtNbrArea_Type=AreaID
_OspfVirtNbrArea_Object=MibTableColumn
ospfVirtNbrArea=_OspfVirtNbrArea_Object((1,3,6,1,2,1,14,11,1,1),_OspfVirtNbrArea_Type())
ospfVirtNbrArea.setMaxAccess(_C)
if mibBuilder.loadTexts:ospfVirtNbrArea.setStatus(_A)
_OspfVirtNbrRtrId_Type=RouterID
_OspfVirtNbrRtrId_Object=MibTableColumn
ospfVirtNbrRtrId=_OspfVirtNbrRtrId_Object((1,3,6,1,2,1,14,11,1,2),_OspfVirtNbrRtrId_Type())
ospfVirtNbrRtrId.setMaxAccess(_C)
if mibBuilder.loadTexts:ospfVirtNbrRtrId.setStatus(_A)
_OspfVirtNbrIpAddr_Type=IpAddress
_OspfVirtNbrIpAddr_Object=MibTableColumn
ospfVirtNbrIpAddr=_OspfVirtNbrIpAddr_Object((1,3,6,1,2,1,14,11,1,3),_OspfVirtNbrIpAddr_Type())
ospfVirtNbrIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ospfVirtNbrIpAddr.setStatus(_A)
_OspfVirtNbrOptions_Type=Integer32
_OspfVirtNbrOptions_Object=MibTableColumn
ospfVirtNbrOptions=_OspfVirtNbrOptions_Object((1,3,6,1,2,1,14,11,1,4),_OspfVirtNbrOptions_Type())
ospfVirtNbrOptions.setMaxAccess(_C)
if mibBuilder.loadTexts:ospfVirtNbrOptions.setStatus(_A)
class _OspfVirtNbrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_L,1),(_q,2),('init',3),(_r,4),(_s,5),(_t,6),(_u,7),('full',8)))
_OspfVirtNbrState_Type.__name__=_E
_OspfVirtNbrState_Object=MibTableColumn
ospfVirtNbrState=_OspfVirtNbrState_Object((1,3,6,1,2,1,14,11,1,5),_OspfVirtNbrState_Type())
ospfVirtNbrState.setMaxAccess(_C)
if mibBuilder.loadTexts:ospfVirtNbrState.setStatus(_A)
_OspfVirtNbrEvents_Type=Counter32
_OspfVirtNbrEvents_Object=MibTableColumn
ospfVirtNbrEvents=_OspfVirtNbrEvents_Object((1,3,6,1,2,1,14,11,1,6),_OspfVirtNbrEvents_Type())
ospfVirtNbrEvents.setMaxAccess(_C)
if mibBuilder.loadTexts:ospfVirtNbrEvents.setStatus(_A)
_OspfVirtNbrLSRetransQLen_Type=Gauge32
_OspfVirtNbrLSRetransQLen_Object=MibTableColumn
ospfVirtNbrLSRetransQLen=_OspfVirtNbrLSRetransQLen_Object((1,3,6,1,2,1,14,11,1,7),_OspfVirtNbrLSRetransQLen_Type())
ospfVirtNbrLSRetransQLen.setMaxAccess(_C)
if mibBuilder.loadTexts:ospfVirtNbrLSRetransQLen.setStatus(_A)
mibBuilder.exportSymbols(_D,**{_f:AreaID,_p:RouterID,'Metric':Metric,'BigMetric':BigMetric,_S:TruthValue,_g:Status,_F:Validation,_K:PositiveInteger,_Q:HelloRange,_I:UpToMaxAge,'InterfaceIndex':InterfaceIndex,_P:DesignatedRouterPriority,'TOSType':TOSType,'ospf':ospf,'ospfGeneralGroup':ospfGeneralGroup,'ospfRouterId':ospfRouterId,'ospfAdminStat':ospfAdminStat,'ospfVersionNumber':ospfVersionNumber,'ospfAreaBdrRtrStatus':ospfAreaBdrRtrStatus,'ospfASBdrRtrStatus':ospfASBdrRtrStatus,'ospfExternLSACount':ospfExternLSACount,'ospfExternLSACksumSum':ospfExternLSACksumSum,'ospfTOSSupport':ospfTOSSupport,'ospfOriginateNewLSAs':ospfOriginateNewLSAs,'ospfRxNewLSAs':ospfRxNewLSAs,'ospfAreaTable':ospfAreaTable,'ospfAreaEntry':ospfAreaEntry,_R:ospfAreaId,'ospfAuthType':ospfAuthType,'ospfImportASExtern':ospfImportASExtern,'ospfSpfRuns':ospfSpfRuns,'ospfAreaBdrRtrCount':ospfAreaBdrRtrCount,'ospfASBdrRtrCount':ospfASBdrRtrCount,'ospfAreaLSACount':ospfAreaLSACount,'ospfAreaLSACksumSum':ospfAreaLSACksumSum,'ospfStubAreaTable':ospfStubAreaTable,'ospfStubAreaEntry':ospfStubAreaEntry,_T:ospfStubAreaID,_U:ospfStubTOS,'ospfStubMetric':ospfStubMetric,'ospfStubStatus':ospfStubStatus,'ospfLsdbTable':ospfLsdbTable,'ospfLsdbEntry':ospfLsdbEntry,_V:ospfLsdbAreaId,_W:ospfLsdbType,_X:ospfLsdbLSID,_Y:ospfLsdbRouterId,'ospfLsdbSequence':ospfLsdbSequence,'ospfLsdbAge':ospfLsdbAge,'ospfLsdbChecksum':ospfLsdbChecksum,'ospfLsdbAdvertisement':ospfLsdbAdvertisement,'ospfAreaRangeTable':ospfAreaRangeTable,'ospfAreaRangeEntry':ospfAreaRangeEntry,_Z:ospfAreaRangeAreaID,_a:ospfAreaRangeNet,'ospfAreaRangeMask':ospfAreaRangeMask,'ospfAreaRangeStatus':ospfAreaRangeStatus,'ospfHostTable':ospfHostTable,'ospfHostEntry':ospfHostEntry,_b:ospfHostIpAddress,_c:ospfHostTOS,'ospfHostMetric':ospfHostMetric,'ospfHostStatus':ospfHostStatus,'ospfIfTable':ospfIfTable,'ospfIfEntry':ospfIfEntry,_d:ospfIfIpAddress,_e:ospfAddressLessIf,'ospfIfAreaId':ospfIfAreaId,'ospfIfType':ospfIfType,'ospfIfAdminStat':ospfIfAdminStat,'ospfIfRtrPriority':ospfIfRtrPriority,'ospfIfTransitDelay':ospfIfTransitDelay,'ospfIfRetransInterval':ospfIfRetransInterval,'ospfIfHelloInterval':ospfIfHelloInterval,'ospfIfRtrDeadInterval':ospfIfRtrDeadInterval,'ospfIfPollInterval':ospfIfPollInterval,'ospfIfState':ospfIfState,'ospfIfDesignatedRouter':ospfIfDesignatedRouter,'ospfIfBackupDesignatedRouter':ospfIfBackupDesignatedRouter,'ospfIfEvents':ospfIfEvents,'ospfIfAuthKey':ospfIfAuthKey,'ospfIfMetricTable':ospfIfMetricTable,'ospfIfMetricEntry':ospfIfMetricEntry,_i:ospfIfMetricIpAddress,_j:ospfIfMetricAddressLessIf,_k:ospfIfMetricTOS,'ospfIfMetricMetric':ospfIfMetricMetric,'ospfIfMetricStatus':ospfIfMetricStatus,'ospfVirtIfTable':ospfVirtIfTable,'ospfVirtIfEntry':ospfVirtIfEntry,_l:ospfVirtIfAreaID,_m:ospfVirtIfNeighbor,'ospfVirtIfTransitDelay':ospfVirtIfTransitDelay,'ospfVirtIfRetransInterval':ospfVirtIfRetransInterval,'ospfVirtIfHelloInterval':ospfVirtIfHelloInterval,'ospfVirtIfRtrDeadInterval':ospfVirtIfRtrDeadInterval,'ospfVirtIfState':ospfVirtIfState,'ospfVirtIfEvents':ospfVirtIfEvents,'ospfVirtIfAuthKey':ospfVirtIfAuthKey,'ospfVirtIfStatus':ospfVirtIfStatus,'ospfNbrTable':ospfNbrTable,'ospfNbrEntry':ospfNbrEntry,_n:ospfNbrIpAddr,_o:ospfNbrAddressLessIndex,'ospfNbrRtrId':ospfNbrRtrId,'ospfNbrOptions':ospfNbrOptions,'ospfNbrPriority':ospfNbrPriority,'ospfNbrState':ospfNbrState,'ospfNbrEvents':ospfNbrEvents,'ospfNbrLSRetransQLen':ospfNbrLSRetransQLen,'ospfNBMANbrStatus':ospfNBMANbrStatus,'ospfVirtNbrTable':ospfVirtNbrTable,'ospfVirtNbrEntry':ospfVirtNbrEntry,_v:ospfVirtNbrArea,_w:ospfVirtNbrRtrId,'ospfVirtNbrIpAddr':ospfVirtNbrIpAddr,'ospfVirtNbrOptions':ospfVirtNbrOptions,'ospfVirtNbrState':ospfVirtNbrState,'ospfVirtNbrEvents':ospfVirtNbrEvents,'ospfVirtNbrLSRetransQLen':ospfVirtNbrLSRetransQLen})