_f='sfpsCallTapFacilityHashIndex'
_e='sfpsBetaFacilityHashIndex'
_d='sfpsUplinkFacilityHashIndex'
_c='sfpsMcastFacilityHashIndex'
_b='notStarted'
_a='faulted'
_Z='pending'
_Y='halted'
_X='running'
_W='enable'
_V='disable'
_U='sfpsRAFacilityHashIndex'
_T='sfpsFpcFacilityHashIndex'
_S='sfpsLiteFacilityHashIndex'
_R='sfpsFabricFacilityHashIndex'
_Q='sfpsDiagFacilityHashIndex'
_P='sfpsVLANFacilityHashIndex'
_O='sfpsVNSFacilityHashIndex'
_N='sfpsCentersFacilityAddress'
_M='kControlEnable'
_L='kControlDisable'
_K='kControlOther'
_J='kStatusNotStarted'
_I='kStatusFaulted'
_H='kStatusPending'
_G='kStatusHalted'
_F='kStatusRunning'
_E='read-write'
_D='CTRON-SFPS-SOFTLINK-MIB'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
sfpsBetaFacility,sfpsCallTapFacility,sfpsCentersFacility,sfpsDiagFacility,sfpsFabricFacility,sfpsFpcFacility,sfpsLiteFacility,sfpsMcastFacility,sfpsRAFacility,sfpsUpLinkFacility,sfpsVLANFacility,sfpsVNSFacility=mibBuilder.importSymbols('CTRON-SFPS-INCLUDE-MIB','sfpsBetaFacility','sfpsCallTapFacility','sfpsCentersFacility','sfpsDiagFacility','sfpsFabricFacility','sfpsFpcFacility','sfpsLiteFacility','sfpsMcastFacility','sfpsRAFacility','sfpsUpLinkFacility','sfpsVLANFacility','sfpsVNSFacility')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class HexInteger(Integer32):0
_SfpsCentersFacilityTable_Object=MibTable
sfpsCentersFacilityTable=_SfpsCentersFacilityTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,1,1))
if mibBuilder.loadTexts:sfpsCentersFacilityTable.setStatus(_A)
_SfpsCentersFacilityEntry_Object=MibTableRow
sfpsCentersFacilityEntry=_SfpsCentersFacilityEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,1,1,1))
sfpsCentersFacilityEntry.setIndexNames((0,_D,_N))
if mibBuilder.loadTexts:sfpsCentersFacilityEntry.setStatus(_A)
_SfpsCentersFacilityAddress_Type=HexInteger
_SfpsCentersFacilityAddress_Object=MibTableColumn
sfpsCentersFacilityAddress=_SfpsCentersFacilityAddress_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,1,1,1,1),_SfpsCentersFacilityAddress_Type())
sfpsCentersFacilityAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCentersFacilityAddress.setStatus(_A)
_SfpsCentersFacilityMetric_Type=Integer32
_SfpsCentersFacilityMetric_Object=MibTableColumn
sfpsCentersFacilityMetric=_SfpsCentersFacilityMetric_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,1,1,1,2),_SfpsCentersFacilityMetric_Type())
sfpsCentersFacilityMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCentersFacilityMetric.setStatus(_A)
_SfpsCentersFacilityElementName_Type=DisplayString
_SfpsCentersFacilityElementName_Object=MibTableColumn
sfpsCentersFacilityElementName=_SfpsCentersFacilityElementName_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,1,1,1,3),_SfpsCentersFacilityElementName_Type())
sfpsCentersFacilityElementName.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCentersFacilityElementName.setStatus(_A)
class _SfpsCentersFacilityOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3),(_I,4),(_J,5)))
_SfpsCentersFacilityOperStatus_Type.__name__=_C
_SfpsCentersFacilityOperStatus_Object=MibTableColumn
sfpsCentersFacilityOperStatus=_SfpsCentersFacilityOperStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,1,1,1,4),_SfpsCentersFacilityOperStatus_Type())
sfpsCentersFacilityOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCentersFacilityOperStatus.setStatus(_A)
class _SfpsCentersFacilityAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3)))
_SfpsCentersFacilityAdminStatus_Type.__name__=_C
_SfpsCentersFacilityAdminStatus_Object=MibTableColumn
sfpsCentersFacilityAdminStatus=_SfpsCentersFacilityAdminStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,1,1,1,5),_SfpsCentersFacilityAdminStatus_Type())
sfpsCentersFacilityAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpsCentersFacilityAdminStatus.setStatus(_A)
_SfpsCentersFacilityStatusTime_Type=TimeTicks
_SfpsCentersFacilityStatusTime_Object=MibTableColumn
sfpsCentersFacilityStatusTime=_SfpsCentersFacilityStatusTime_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,1,1,1,6),_SfpsCentersFacilityStatusTime_Type())
sfpsCentersFacilityStatusTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCentersFacilityStatusTime.setStatus(_A)
_SfpsCentersFacilityRequests_Type=Integer32
_SfpsCentersFacilityRequests_Object=MibTableColumn
sfpsCentersFacilityRequests=_SfpsCentersFacilityRequests_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,1,1,1,7),_SfpsCentersFacilityRequests_Type())
sfpsCentersFacilityRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCentersFacilityRequests.setStatus(_A)
_SfpsCentersFacilityResponses_Type=Integer32
_SfpsCentersFacilityResponses_Object=MibTableColumn
sfpsCentersFacilityResponses=_SfpsCentersFacilityResponses_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,1,1,1,8),_SfpsCentersFacilityResponses_Type())
sfpsCentersFacilityResponses.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCentersFacilityResponses.setStatus(_A)
_SfpsVNSFacilityTable_Object=MibTable
sfpsVNSFacilityTable=_SfpsVNSFacilityTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,2,1))
if mibBuilder.loadTexts:sfpsVNSFacilityTable.setStatus(_A)
_SfpsVNSFacilityEntry_Object=MibTableRow
sfpsVNSFacilityEntry=_SfpsVNSFacilityEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,2,1,1))
sfpsVNSFacilityEntry.setIndexNames((0,_D,_O))
if mibBuilder.loadTexts:sfpsVNSFacilityEntry.setStatus(_A)
_SfpsVNSFacilityHashIndex_Type=Integer32
_SfpsVNSFacilityHashIndex_Object=MibTableColumn
sfpsVNSFacilityHashIndex=_SfpsVNSFacilityHashIndex_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,2,1,1,1),_SfpsVNSFacilityHashIndex_Type())
sfpsVNSFacilityHashIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsVNSFacilityHashIndex.setStatus(_A)
_SfpsVNSFacilityElementName_Type=DisplayString
_SfpsVNSFacilityElementName_Object=MibTableColumn
sfpsVNSFacilityElementName=_SfpsVNSFacilityElementName_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,2,1,1,2),_SfpsVNSFacilityElementName_Type())
sfpsVNSFacilityElementName.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsVNSFacilityElementName.setStatus(_A)
class _SfpsVNSFacilityAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3)))
_SfpsVNSFacilityAdminStatus_Type.__name__=_C
_SfpsVNSFacilityAdminStatus_Object=MibTableColumn
sfpsVNSFacilityAdminStatus=_SfpsVNSFacilityAdminStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,2,1,1,3),_SfpsVNSFacilityAdminStatus_Type())
sfpsVNSFacilityAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpsVNSFacilityAdminStatus.setStatus(_A)
class _SfpsVNSFacilityOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3),(_I,4),(_J,5)))
_SfpsVNSFacilityOperStatus_Type.__name__=_C
_SfpsVNSFacilityOperStatus_Object=MibTableColumn
sfpsVNSFacilityOperStatus=_SfpsVNSFacilityOperStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,2,1,1,4),_SfpsVNSFacilityOperStatus_Type())
sfpsVNSFacilityOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsVNSFacilityOperStatus.setStatus(_A)
_SfpsVNSFacilityStatusTime_Type=TimeTicks
_SfpsVNSFacilityStatusTime_Object=MibTableColumn
sfpsVNSFacilityStatusTime=_SfpsVNSFacilityStatusTime_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,2,1,1,5),_SfpsVNSFacilityStatusTime_Type())
sfpsVNSFacilityStatusTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsVNSFacilityStatusTime.setStatus(_A)
_SfpsVLANFacilityTable_Object=MibTable
sfpsVLANFacilityTable=_SfpsVLANFacilityTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,3,1))
if mibBuilder.loadTexts:sfpsVLANFacilityTable.setStatus(_A)
_SfpsVLANFacilityEntry_Object=MibTableRow
sfpsVLANFacilityEntry=_SfpsVLANFacilityEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,3,1,1))
sfpsVLANFacilityEntry.setIndexNames((0,_D,_P))
if mibBuilder.loadTexts:sfpsVLANFacilityEntry.setStatus(_A)
_SfpsVLANFacilityHashIndex_Type=Integer32
_SfpsVLANFacilityHashIndex_Object=MibTableColumn
sfpsVLANFacilityHashIndex=_SfpsVLANFacilityHashIndex_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,3,1,1,1),_SfpsVLANFacilityHashIndex_Type())
sfpsVLANFacilityHashIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsVLANFacilityHashIndex.setStatus(_A)
_SfpsVLANFacilityElementName_Type=DisplayString
_SfpsVLANFacilityElementName_Object=MibTableColumn
sfpsVLANFacilityElementName=_SfpsVLANFacilityElementName_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,3,1,1,2),_SfpsVLANFacilityElementName_Type())
sfpsVLANFacilityElementName.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsVLANFacilityElementName.setStatus(_A)
class _SfpsVLANFacilityAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3)))
_SfpsVLANFacilityAdminStatus_Type.__name__=_C
_SfpsVLANFacilityAdminStatus_Object=MibTableColumn
sfpsVLANFacilityAdminStatus=_SfpsVLANFacilityAdminStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,3,1,1,3),_SfpsVLANFacilityAdminStatus_Type())
sfpsVLANFacilityAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpsVLANFacilityAdminStatus.setStatus(_A)
class _SfpsVLANFacilityOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3),(_I,4),(_J,5)))
_SfpsVLANFacilityOperStatus_Type.__name__=_C
_SfpsVLANFacilityOperStatus_Object=MibTableColumn
sfpsVLANFacilityOperStatus=_SfpsVLANFacilityOperStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,3,1,1,4),_SfpsVLANFacilityOperStatus_Type())
sfpsVLANFacilityOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsVLANFacilityOperStatus.setStatus(_A)
_SfpsVLANFacilityStatusTime_Type=TimeTicks
_SfpsVLANFacilityStatusTime_Object=MibTableColumn
sfpsVLANFacilityStatusTime=_SfpsVLANFacilityStatusTime_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,3,1,1,5),_SfpsVLANFacilityStatusTime_Type())
sfpsVLANFacilityStatusTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsVLANFacilityStatusTime.setStatus(_A)
_SfpsDiagFacilityTable_Object=MibTable
sfpsDiagFacilityTable=_SfpsDiagFacilityTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,4,1))
if mibBuilder.loadTexts:sfpsDiagFacilityTable.setStatus(_A)
_SfpsDiagFacilityEntry_Object=MibTableRow
sfpsDiagFacilityEntry=_SfpsDiagFacilityEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,4,1,1))
sfpsDiagFacilityEntry.setIndexNames((0,_D,_Q))
if mibBuilder.loadTexts:sfpsDiagFacilityEntry.setStatus(_A)
_SfpsDiagFacilityHashIndex_Type=Integer32
_SfpsDiagFacilityHashIndex_Object=MibTableColumn
sfpsDiagFacilityHashIndex=_SfpsDiagFacilityHashIndex_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,4,1,1,1),_SfpsDiagFacilityHashIndex_Type())
sfpsDiagFacilityHashIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDiagFacilityHashIndex.setStatus(_A)
_SfpsDiagFacilityElementName_Type=DisplayString
_SfpsDiagFacilityElementName_Object=MibTableColumn
sfpsDiagFacilityElementName=_SfpsDiagFacilityElementName_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,4,1,1,2),_SfpsDiagFacilityElementName_Type())
sfpsDiagFacilityElementName.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDiagFacilityElementName.setStatus(_A)
class _SfpsDiagFacilityAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3)))
_SfpsDiagFacilityAdminStatus_Type.__name__=_C
_SfpsDiagFacilityAdminStatus_Object=MibTableColumn
sfpsDiagFacilityAdminStatus=_SfpsDiagFacilityAdminStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,4,1,1,3),_SfpsDiagFacilityAdminStatus_Type())
sfpsDiagFacilityAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpsDiagFacilityAdminStatus.setStatus(_A)
class _SfpsDiagFacilityOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3),(_I,4),(_J,5)))
_SfpsDiagFacilityOperStatus_Type.__name__=_C
_SfpsDiagFacilityOperStatus_Object=MibTableColumn
sfpsDiagFacilityOperStatus=_SfpsDiagFacilityOperStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,4,1,1,4),_SfpsDiagFacilityOperStatus_Type())
sfpsDiagFacilityOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDiagFacilityOperStatus.setStatus(_A)
_SfpsDiagFacilityStatusTime_Type=TimeTicks
_SfpsDiagFacilityStatusTime_Object=MibTableColumn
sfpsDiagFacilityStatusTime=_SfpsDiagFacilityStatusTime_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,4,1,1,5),_SfpsDiagFacilityStatusTime_Type())
sfpsDiagFacilityStatusTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDiagFacilityStatusTime.setStatus(_A)
_SfpsFabricFacilityTable_Object=MibTable
sfpsFabricFacilityTable=_SfpsFabricFacilityTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,6,1))
if mibBuilder.loadTexts:sfpsFabricFacilityTable.setStatus(_A)
_SfpsFabricFacilityEntry_Object=MibTableRow
sfpsFabricFacilityEntry=_SfpsFabricFacilityEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,6,1,1))
sfpsFabricFacilityEntry.setIndexNames((0,_D,_R))
if mibBuilder.loadTexts:sfpsFabricFacilityEntry.setStatus(_A)
_SfpsFabricFacilityHashIndex_Type=Integer32
_SfpsFabricFacilityHashIndex_Object=MibTableColumn
sfpsFabricFacilityHashIndex=_SfpsFabricFacilityHashIndex_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,6,1,1,1),_SfpsFabricFacilityHashIndex_Type())
sfpsFabricFacilityHashIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsFabricFacilityHashIndex.setStatus(_A)
_SfpsFabricFacilityElementName_Type=DisplayString
_SfpsFabricFacilityElementName_Object=MibTableColumn
sfpsFabricFacilityElementName=_SfpsFabricFacilityElementName_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,6,1,1,2),_SfpsFabricFacilityElementName_Type())
sfpsFabricFacilityElementName.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsFabricFacilityElementName.setStatus(_A)
class _SfpsFabricFacilityAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3)))
_SfpsFabricFacilityAdminStatus_Type.__name__=_C
_SfpsFabricFacilityAdminStatus_Object=MibTableColumn
sfpsFabricFacilityAdminStatus=_SfpsFabricFacilityAdminStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,6,1,1,3),_SfpsFabricFacilityAdminStatus_Type())
sfpsFabricFacilityAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpsFabricFacilityAdminStatus.setStatus(_A)
class _SfpsFabricFacilityOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3),(_I,4),(_J,5)))
_SfpsFabricFacilityOperStatus_Type.__name__=_C
_SfpsFabricFacilityOperStatus_Object=MibTableColumn
sfpsFabricFacilityOperStatus=_SfpsFabricFacilityOperStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,6,1,1,4),_SfpsFabricFacilityOperStatus_Type())
sfpsFabricFacilityOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsFabricFacilityOperStatus.setStatus(_A)
_SfpsFabricFacilityStatusTime_Type=TimeTicks
_SfpsFabricFacilityStatusTime_Object=MibTableColumn
sfpsFabricFacilityStatusTime=_SfpsFabricFacilityStatusTime_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,6,1,1,5),_SfpsFabricFacilityStatusTime_Type())
sfpsFabricFacilityStatusTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsFabricFacilityStatusTime.setStatus(_A)
_SfpsLiteFacilityTable_Object=MibTable
sfpsLiteFacilityTable=_SfpsLiteFacilityTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,7,1))
if mibBuilder.loadTexts:sfpsLiteFacilityTable.setStatus(_A)
_SfpsLiteFacilityEntry_Object=MibTableRow
sfpsLiteFacilityEntry=_SfpsLiteFacilityEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,7,1,1))
sfpsLiteFacilityEntry.setIndexNames((0,_D,_S))
if mibBuilder.loadTexts:sfpsLiteFacilityEntry.setStatus(_A)
_SfpsLiteFacilityHashIndex_Type=Integer32
_SfpsLiteFacilityHashIndex_Object=MibTableColumn
sfpsLiteFacilityHashIndex=_SfpsLiteFacilityHashIndex_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,7,1,1,1),_SfpsLiteFacilityHashIndex_Type())
sfpsLiteFacilityHashIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsLiteFacilityHashIndex.setStatus(_A)
_SfpsLiteFacilityElementName_Type=DisplayString
_SfpsLiteFacilityElementName_Object=MibTableColumn
sfpsLiteFacilityElementName=_SfpsLiteFacilityElementName_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,7,1,1,2),_SfpsLiteFacilityElementName_Type())
sfpsLiteFacilityElementName.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsLiteFacilityElementName.setStatus(_A)
class _SfpsLiteFacilityAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3)))
_SfpsLiteFacilityAdminStatus_Type.__name__=_C
_SfpsLiteFacilityAdminStatus_Object=MibTableColumn
sfpsLiteFacilityAdminStatus=_SfpsLiteFacilityAdminStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,7,1,1,3),_SfpsLiteFacilityAdminStatus_Type())
sfpsLiteFacilityAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpsLiteFacilityAdminStatus.setStatus(_A)
class _SfpsLiteFacilityOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3),(_I,4),(_J,5)))
_SfpsLiteFacilityOperStatus_Type.__name__=_C
_SfpsLiteFacilityOperStatus_Object=MibTableColumn
sfpsLiteFacilityOperStatus=_SfpsLiteFacilityOperStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,7,1,1,4),_SfpsLiteFacilityOperStatus_Type())
sfpsLiteFacilityOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsLiteFacilityOperStatus.setStatus(_A)
_SfpsLiteFacilityStatusTime_Type=TimeTicks
_SfpsLiteFacilityStatusTime_Object=MibTableColumn
sfpsLiteFacilityStatusTime=_SfpsLiteFacilityStatusTime_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,7,1,1,5),_SfpsLiteFacilityStatusTime_Type())
sfpsLiteFacilityStatusTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsLiteFacilityStatusTime.setStatus(_A)
_SfpsFpcFacilityTable_Object=MibTable
sfpsFpcFacilityTable=_SfpsFpcFacilityTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,8,1))
if mibBuilder.loadTexts:sfpsFpcFacilityTable.setStatus(_A)
_SfpsFpcFacilityEntry_Object=MibTableRow
sfpsFpcFacilityEntry=_SfpsFpcFacilityEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,8,1,1))
sfpsFpcFacilityEntry.setIndexNames((0,_D,_T))
if mibBuilder.loadTexts:sfpsFpcFacilityEntry.setStatus(_A)
_SfpsFpcFacilityHashIndex_Type=Integer32
_SfpsFpcFacilityHashIndex_Object=MibTableColumn
sfpsFpcFacilityHashIndex=_SfpsFpcFacilityHashIndex_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,8,1,1,1),_SfpsFpcFacilityHashIndex_Type())
sfpsFpcFacilityHashIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsFpcFacilityHashIndex.setStatus(_A)
_SfpsFpcFacilityElementName_Type=DisplayString
_SfpsFpcFacilityElementName_Object=MibTableColumn
sfpsFpcFacilityElementName=_SfpsFpcFacilityElementName_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,8,1,1,2),_SfpsFpcFacilityElementName_Type())
sfpsFpcFacilityElementName.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsFpcFacilityElementName.setStatus(_A)
class _SfpsFpcFacilityAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3)))
_SfpsFpcFacilityAdminStatus_Type.__name__=_C
_SfpsFpcFacilityAdminStatus_Object=MibTableColumn
sfpsFpcFacilityAdminStatus=_SfpsFpcFacilityAdminStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,8,1,1,3),_SfpsFpcFacilityAdminStatus_Type())
sfpsFpcFacilityAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpsFpcFacilityAdminStatus.setStatus(_A)
class _SfpsFpcFacilityOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3),(_I,4),(_J,5)))
_SfpsFpcFacilityOperStatus_Type.__name__=_C
_SfpsFpcFacilityOperStatus_Object=MibTableColumn
sfpsFpcFacilityOperStatus=_SfpsFpcFacilityOperStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,8,1,1,4),_SfpsFpcFacilityOperStatus_Type())
sfpsFpcFacilityOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsFpcFacilityOperStatus.setStatus(_A)
_SfpsFpcFacilityStatusTime_Type=TimeTicks
_SfpsFpcFacilityStatusTime_Object=MibTableColumn
sfpsFpcFacilityStatusTime=_SfpsFpcFacilityStatusTime_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,8,1,1,5),_SfpsFpcFacilityStatusTime_Type())
sfpsFpcFacilityStatusTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsFpcFacilityStatusTime.setStatus(_A)
_SfpsRAFacilityTable_Object=MibTable
sfpsRAFacilityTable=_SfpsRAFacilityTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,14,1))
if mibBuilder.loadTexts:sfpsRAFacilityTable.setStatus(_A)
_SfpsRAFacilityEntry_Object=MibTableRow
sfpsRAFacilityEntry=_SfpsRAFacilityEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,14,1,1))
sfpsRAFacilityEntry.setIndexNames((0,_D,_U))
if mibBuilder.loadTexts:sfpsRAFacilityEntry.setStatus(_A)
_SfpsRAFacilityHashIndex_Type=Integer32
_SfpsRAFacilityHashIndex_Object=MibTableColumn
sfpsRAFacilityHashIndex=_SfpsRAFacilityHashIndex_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,14,1,1,1),_SfpsRAFacilityHashIndex_Type())
sfpsRAFacilityHashIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsRAFacilityHashIndex.setStatus(_A)
_SfpsRAFacilityName_Type=DisplayString
_SfpsRAFacilityName_Object=MibTableColumn
sfpsRAFacilityName=_SfpsRAFacilityName_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,14,1,1,2),_SfpsRAFacilityName_Type())
sfpsRAFacilityName.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsRAFacilityName.setStatus(_A)
class _SfpsRAFacilityAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),(_V,2),(_W,3)))
_SfpsRAFacilityAdminStatus_Type.__name__=_C
_SfpsRAFacilityAdminStatus_Object=MibTableColumn
sfpsRAFacilityAdminStatus=_SfpsRAFacilityAdminStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,14,1,1,3),_SfpsRAFacilityAdminStatus_Type())
sfpsRAFacilityAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpsRAFacilityAdminStatus.setStatus(_A)
class _SfpsRAFacilityOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_X,1),(_Y,2),(_Z,3),(_a,4),(_b,5)))
_SfpsRAFacilityOperStatus_Type.__name__=_C
_SfpsRAFacilityOperStatus_Object=MibTableColumn
sfpsRAFacilityOperStatus=_SfpsRAFacilityOperStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,14,1,1,4),_SfpsRAFacilityOperStatus_Type())
sfpsRAFacilityOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsRAFacilityOperStatus.setStatus(_A)
_SfpsRAFacilityStatusTime_Type=TimeTicks
_SfpsRAFacilityStatusTime_Object=MibTableColumn
sfpsRAFacilityStatusTime=_SfpsRAFacilityStatusTime_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,14,1,1,5),_SfpsRAFacilityStatusTime_Type())
sfpsRAFacilityStatusTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsRAFacilityStatusTime.setStatus(_A)
_SfpsMcastFacilityTable_Object=MibTable
sfpsMcastFacilityTable=_SfpsMcastFacilityTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,15,1))
if mibBuilder.loadTexts:sfpsMcastFacilityTable.setStatus(_A)
_SfpsMcastFacilityEntry_Object=MibTableRow
sfpsMcastFacilityEntry=_SfpsMcastFacilityEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,15,1,1))
sfpsMcastFacilityEntry.setIndexNames((0,_D,_c))
if mibBuilder.loadTexts:sfpsMcastFacilityEntry.setStatus(_A)
_SfpsMcastFacilityHashIndex_Type=Integer32
_SfpsMcastFacilityHashIndex_Object=MibTableColumn
sfpsMcastFacilityHashIndex=_SfpsMcastFacilityHashIndex_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,15,1,1,1),_SfpsMcastFacilityHashIndex_Type())
sfpsMcastFacilityHashIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMcastFacilityHashIndex.setStatus(_A)
_SfpsMcastFacilityElementName_Type=DisplayString
_SfpsMcastFacilityElementName_Object=MibTableColumn
sfpsMcastFacilityElementName=_SfpsMcastFacilityElementName_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,15,1,1,2),_SfpsMcastFacilityElementName_Type())
sfpsMcastFacilityElementName.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMcastFacilityElementName.setStatus(_A)
class _SfpsMcastFacilityAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3)))
_SfpsMcastFacilityAdminStatus_Type.__name__=_C
_SfpsMcastFacilityAdminStatus_Object=MibTableColumn
sfpsMcastFacilityAdminStatus=_SfpsMcastFacilityAdminStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,15,1,1,3),_SfpsMcastFacilityAdminStatus_Type())
sfpsMcastFacilityAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpsMcastFacilityAdminStatus.setStatus(_A)
class _SfpsMcastFacilityOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3),(_I,4),(_J,5)))
_SfpsMcastFacilityOperStatus_Type.__name__=_C
_SfpsMcastFacilityOperStatus_Object=MibTableColumn
sfpsMcastFacilityOperStatus=_SfpsMcastFacilityOperStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,15,1,1,4),_SfpsMcastFacilityOperStatus_Type())
sfpsMcastFacilityOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMcastFacilityOperStatus.setStatus(_A)
_SfpsMcastFacilityStatusTime_Type=TimeTicks
_SfpsMcastFacilityStatusTime_Object=MibTableColumn
sfpsMcastFacilityStatusTime=_SfpsMcastFacilityStatusTime_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,15,1,1,5),_SfpsMcastFacilityStatusTime_Type())
sfpsMcastFacilityStatusTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMcastFacilityStatusTime.setStatus(_A)
_SfpsUplinkFacilityTable_Object=MibTable
sfpsUplinkFacilityTable=_SfpsUplinkFacilityTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,16,1))
if mibBuilder.loadTexts:sfpsUplinkFacilityTable.setStatus(_A)
_SfpsUplinkFacilityEntry_Object=MibTableRow
sfpsUplinkFacilityEntry=_SfpsUplinkFacilityEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,16,1,1))
sfpsUplinkFacilityEntry.setIndexNames((0,_D,_d))
if mibBuilder.loadTexts:sfpsUplinkFacilityEntry.setStatus(_A)
_SfpsUplinkFacilityHashIndex_Type=Integer32
_SfpsUplinkFacilityHashIndex_Object=MibTableColumn
sfpsUplinkFacilityHashIndex=_SfpsUplinkFacilityHashIndex_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,16,1,1,1),_SfpsUplinkFacilityHashIndex_Type())
sfpsUplinkFacilityHashIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsUplinkFacilityHashIndex.setStatus(_A)
_SfpsUplinkFacilityName_Type=DisplayString
_SfpsUplinkFacilityName_Object=MibTableColumn
sfpsUplinkFacilityName=_SfpsUplinkFacilityName_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,16,1,1,2),_SfpsUplinkFacilityName_Type())
sfpsUplinkFacilityName.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsUplinkFacilityName.setStatus(_A)
class _SfpsUplinkFacilityAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),(_V,2),(_W,3)))
_SfpsUplinkFacilityAdminStatus_Type.__name__=_C
_SfpsUplinkFacilityAdminStatus_Object=MibTableColumn
sfpsUplinkFacilityAdminStatus=_SfpsUplinkFacilityAdminStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,16,1,1,3),_SfpsUplinkFacilityAdminStatus_Type())
sfpsUplinkFacilityAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpsUplinkFacilityAdminStatus.setStatus(_A)
class _SfpsUplinkFacilityOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_X,1),(_Y,2),(_Z,3),(_a,4),(_b,5)))
_SfpsUplinkFacilityOperStatus_Type.__name__=_C
_SfpsUplinkFacilityOperStatus_Object=MibTableColumn
sfpsUplinkFacilityOperStatus=_SfpsUplinkFacilityOperStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,16,1,1,4),_SfpsUplinkFacilityOperStatus_Type())
sfpsUplinkFacilityOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsUplinkFacilityOperStatus.setStatus(_A)
_SfpsUplinkFacilityStatusTime_Type=TimeTicks
_SfpsUplinkFacilityStatusTime_Object=MibTableColumn
sfpsUplinkFacilityStatusTime=_SfpsUplinkFacilityStatusTime_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,16,1,1,5),_SfpsUplinkFacilityStatusTime_Type())
sfpsUplinkFacilityStatusTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsUplinkFacilityStatusTime.setStatus(_A)
_SfpsBetaFacilityTable_Object=MibTable
sfpsBetaFacilityTable=_SfpsBetaFacilityTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,21,1))
if mibBuilder.loadTexts:sfpsBetaFacilityTable.setStatus(_A)
_SfpsBetaFacilityEntry_Object=MibTableRow
sfpsBetaFacilityEntry=_SfpsBetaFacilityEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,21,1,1))
sfpsBetaFacilityEntry.setIndexNames((0,_D,_e))
if mibBuilder.loadTexts:sfpsBetaFacilityEntry.setStatus(_A)
_SfpsBetaFacilityHashIndex_Type=Integer32
_SfpsBetaFacilityHashIndex_Object=MibTableColumn
sfpsBetaFacilityHashIndex=_SfpsBetaFacilityHashIndex_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,21,1,1,1),_SfpsBetaFacilityHashIndex_Type())
sfpsBetaFacilityHashIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBetaFacilityHashIndex.setStatus(_A)
_SfpsBetaFacilityElementName_Type=DisplayString
_SfpsBetaFacilityElementName_Object=MibTableColumn
sfpsBetaFacilityElementName=_SfpsBetaFacilityElementName_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,21,1,1,2),_SfpsBetaFacilityElementName_Type())
sfpsBetaFacilityElementName.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBetaFacilityElementName.setStatus(_A)
class _SfpsBetaFacilityAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3)))
_SfpsBetaFacilityAdminStatus_Type.__name__=_C
_SfpsBetaFacilityAdminStatus_Object=MibTableColumn
sfpsBetaFacilityAdminStatus=_SfpsBetaFacilityAdminStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,21,1,1,3),_SfpsBetaFacilityAdminStatus_Type())
sfpsBetaFacilityAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpsBetaFacilityAdminStatus.setStatus(_A)
class _SfpsBetaFacilityOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3),(_I,4),(_J,5)))
_SfpsBetaFacilityOperStatus_Type.__name__=_C
_SfpsBetaFacilityOperStatus_Object=MibTableColumn
sfpsBetaFacilityOperStatus=_SfpsBetaFacilityOperStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,21,1,1,4),_SfpsBetaFacilityOperStatus_Type())
sfpsBetaFacilityOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBetaFacilityOperStatus.setStatus(_A)
_SfpsBetaFacilityStatusTime_Type=TimeTicks
_SfpsBetaFacilityStatusTime_Object=MibTableColumn
sfpsBetaFacilityStatusTime=_SfpsBetaFacilityStatusTime_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,21,1,1,5),_SfpsBetaFacilityStatusTime_Type())
sfpsBetaFacilityStatusTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBetaFacilityStatusTime.setStatus(_A)
_SfpsCallTapFacilityTable_Object=MibTable
sfpsCallTapFacilityTable=_SfpsCallTapFacilityTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,32,1))
if mibBuilder.loadTexts:sfpsCallTapFacilityTable.setStatus(_A)
_SfpsCallTapFacilityEntry_Object=MibTableRow
sfpsCallTapFacilityEntry=_SfpsCallTapFacilityEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,32,1,1))
sfpsCallTapFacilityEntry.setIndexNames((0,_D,_f))
if mibBuilder.loadTexts:sfpsCallTapFacilityEntry.setStatus(_A)
_SfpsCallTapFacilityHashIndex_Type=Integer32
_SfpsCallTapFacilityHashIndex_Object=MibTableColumn
sfpsCallTapFacilityHashIndex=_SfpsCallTapFacilityHashIndex_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,32,1,1,1),_SfpsCallTapFacilityHashIndex_Type())
sfpsCallTapFacilityHashIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCallTapFacilityHashIndex.setStatus(_A)
_SfpsCallTapFacilityElementName_Type=DisplayString
_SfpsCallTapFacilityElementName_Object=MibTableColumn
sfpsCallTapFacilityElementName=_SfpsCallTapFacilityElementName_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,32,1,1,2),_SfpsCallTapFacilityElementName_Type())
sfpsCallTapFacilityElementName.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCallTapFacilityElementName.setStatus(_A)
class _SfpsCallTapFacilityAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3)))
_SfpsCallTapFacilityAdminStatus_Type.__name__=_C
_SfpsCallTapFacilityAdminStatus_Object=MibTableColumn
sfpsCallTapFacilityAdminStatus=_SfpsCallTapFacilityAdminStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,32,1,1,3),_SfpsCallTapFacilityAdminStatus_Type())
sfpsCallTapFacilityAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpsCallTapFacilityAdminStatus.setStatus(_A)
class _SfpsCallTapFacilityOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3),(_I,4),(_J,5)))
_SfpsCallTapFacilityOperStatus_Type.__name__=_C
_SfpsCallTapFacilityOperStatus_Object=MibTableColumn
sfpsCallTapFacilityOperStatus=_SfpsCallTapFacilityOperStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,32,1,1,4),_SfpsCallTapFacilityOperStatus_Type())
sfpsCallTapFacilityOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCallTapFacilityOperStatus.setStatus(_A)
_SfpsCallTapFacilityStatusTime_Type=TimeTicks
_SfpsCallTapFacilityStatusTime_Object=MibTableColumn
sfpsCallTapFacilityStatusTime=_SfpsCallTapFacilityStatusTime_Object((1,3,6,1,4,1,52,4,2,4,2,2,11,32,1,1,5),_SfpsCallTapFacilityStatusTime_Type())
sfpsCallTapFacilityStatusTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCallTapFacilityStatusTime.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'HexInteger':HexInteger,'sfpsCentersFacilityTable':sfpsCentersFacilityTable,'sfpsCentersFacilityEntry':sfpsCentersFacilityEntry,_N:sfpsCentersFacilityAddress,'sfpsCentersFacilityMetric':sfpsCentersFacilityMetric,'sfpsCentersFacilityElementName':sfpsCentersFacilityElementName,'sfpsCentersFacilityOperStatus':sfpsCentersFacilityOperStatus,'sfpsCentersFacilityAdminStatus':sfpsCentersFacilityAdminStatus,'sfpsCentersFacilityStatusTime':sfpsCentersFacilityStatusTime,'sfpsCentersFacilityRequests':sfpsCentersFacilityRequests,'sfpsCentersFacilityResponses':sfpsCentersFacilityResponses,'sfpsVNSFacilityTable':sfpsVNSFacilityTable,'sfpsVNSFacilityEntry':sfpsVNSFacilityEntry,_O:sfpsVNSFacilityHashIndex,'sfpsVNSFacilityElementName':sfpsVNSFacilityElementName,'sfpsVNSFacilityAdminStatus':sfpsVNSFacilityAdminStatus,'sfpsVNSFacilityOperStatus':sfpsVNSFacilityOperStatus,'sfpsVNSFacilityStatusTime':sfpsVNSFacilityStatusTime,'sfpsVLANFacilityTable':sfpsVLANFacilityTable,'sfpsVLANFacilityEntry':sfpsVLANFacilityEntry,_P:sfpsVLANFacilityHashIndex,'sfpsVLANFacilityElementName':sfpsVLANFacilityElementName,'sfpsVLANFacilityAdminStatus':sfpsVLANFacilityAdminStatus,'sfpsVLANFacilityOperStatus':sfpsVLANFacilityOperStatus,'sfpsVLANFacilityStatusTime':sfpsVLANFacilityStatusTime,'sfpsDiagFacilityTable':sfpsDiagFacilityTable,'sfpsDiagFacilityEntry':sfpsDiagFacilityEntry,_Q:sfpsDiagFacilityHashIndex,'sfpsDiagFacilityElementName':sfpsDiagFacilityElementName,'sfpsDiagFacilityAdminStatus':sfpsDiagFacilityAdminStatus,'sfpsDiagFacilityOperStatus':sfpsDiagFacilityOperStatus,'sfpsDiagFacilityStatusTime':sfpsDiagFacilityStatusTime,'sfpsFabricFacilityTable':sfpsFabricFacilityTable,'sfpsFabricFacilityEntry':sfpsFabricFacilityEntry,_R:sfpsFabricFacilityHashIndex,'sfpsFabricFacilityElementName':sfpsFabricFacilityElementName,'sfpsFabricFacilityAdminStatus':sfpsFabricFacilityAdminStatus,'sfpsFabricFacilityOperStatus':sfpsFabricFacilityOperStatus,'sfpsFabricFacilityStatusTime':sfpsFabricFacilityStatusTime,'sfpsLiteFacilityTable':sfpsLiteFacilityTable,'sfpsLiteFacilityEntry':sfpsLiteFacilityEntry,_S:sfpsLiteFacilityHashIndex,'sfpsLiteFacilityElementName':sfpsLiteFacilityElementName,'sfpsLiteFacilityAdminStatus':sfpsLiteFacilityAdminStatus,'sfpsLiteFacilityOperStatus':sfpsLiteFacilityOperStatus,'sfpsLiteFacilityStatusTime':sfpsLiteFacilityStatusTime,'sfpsFpcFacilityTable':sfpsFpcFacilityTable,'sfpsFpcFacilityEntry':sfpsFpcFacilityEntry,_T:sfpsFpcFacilityHashIndex,'sfpsFpcFacilityElementName':sfpsFpcFacilityElementName,'sfpsFpcFacilityAdminStatus':sfpsFpcFacilityAdminStatus,'sfpsFpcFacilityOperStatus':sfpsFpcFacilityOperStatus,'sfpsFpcFacilityStatusTime':sfpsFpcFacilityStatusTime,'sfpsRAFacilityTable':sfpsRAFacilityTable,'sfpsRAFacilityEntry':sfpsRAFacilityEntry,_U:sfpsRAFacilityHashIndex,'sfpsRAFacilityName':sfpsRAFacilityName,'sfpsRAFacilityAdminStatus':sfpsRAFacilityAdminStatus,'sfpsRAFacilityOperStatus':sfpsRAFacilityOperStatus,'sfpsRAFacilityStatusTime':sfpsRAFacilityStatusTime,'sfpsMcastFacilityTable':sfpsMcastFacilityTable,'sfpsMcastFacilityEntry':sfpsMcastFacilityEntry,_c:sfpsMcastFacilityHashIndex,'sfpsMcastFacilityElementName':sfpsMcastFacilityElementName,'sfpsMcastFacilityAdminStatus':sfpsMcastFacilityAdminStatus,'sfpsMcastFacilityOperStatus':sfpsMcastFacilityOperStatus,'sfpsMcastFacilityStatusTime':sfpsMcastFacilityStatusTime,'sfpsUplinkFacilityTable':sfpsUplinkFacilityTable,'sfpsUplinkFacilityEntry':sfpsUplinkFacilityEntry,_d:sfpsUplinkFacilityHashIndex,'sfpsUplinkFacilityName':sfpsUplinkFacilityName,'sfpsUplinkFacilityAdminStatus':sfpsUplinkFacilityAdminStatus,'sfpsUplinkFacilityOperStatus':sfpsUplinkFacilityOperStatus,'sfpsUplinkFacilityStatusTime':sfpsUplinkFacilityStatusTime,'sfpsBetaFacilityTable':sfpsBetaFacilityTable,'sfpsBetaFacilityEntry':sfpsBetaFacilityEntry,_e:sfpsBetaFacilityHashIndex,'sfpsBetaFacilityElementName':sfpsBetaFacilityElementName,'sfpsBetaFacilityAdminStatus':sfpsBetaFacilityAdminStatus,'sfpsBetaFacilityOperStatus':sfpsBetaFacilityOperStatus,'sfpsBetaFacilityStatusTime':sfpsBetaFacilityStatusTime,'sfpsCallTapFacilityTable':sfpsCallTapFacilityTable,'sfpsCallTapFacilityEntry':sfpsCallTapFacilityEntry,_f:sfpsCallTapFacilityHashIndex,'sfpsCallTapFacilityElementName':sfpsCallTapFacilityElementName,'sfpsCallTapFacilityAdminStatus':sfpsCallTapFacilityAdminStatus,'sfpsCallTapFacilityOperStatus':sfpsCallTapFacilityOperStatus,'sfpsCallTapFacilityStatusTime':sfpsCallTapFacilityStatusTime})