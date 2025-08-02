_G='sfpsResolveCounterTableSource'
_F='sfpsServiceCenterFloodAddress'
_E='CTRON-SFPS-FLOOD-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
sfpsISPFlood,sfpsMobileUserReset,sfpsMobileUserTable,sfpsResolveCounter=mibBuilder.importSymbols('CTRON-SFPS-INCLUDE-MIB','sfpsISPFlood','sfpsMobileUserReset','sfpsMobileUserTable','sfpsResolveCounter')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class HexInteger(Integer32):0
class SfpsAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_SfpsServiceCenterFloodTable_Object=MibTable
sfpsServiceCenterFloodTable=_SfpsServiceCenterFloodTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,6,1))
if mibBuilder.loadTexts:sfpsServiceCenterFloodTable.setStatus(_A)
_SfpsServiceCenterFloodEntry_Object=MibTableRow
sfpsServiceCenterFloodEntry=_SfpsServiceCenterFloodEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,6,1,1))
sfpsServiceCenterFloodEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:sfpsServiceCenterFloodEntry.setStatus(_A)
_SfpsServiceCenterFloodAddress_Type=HexInteger
_SfpsServiceCenterFloodAddress_Object=MibTableColumn
sfpsServiceCenterFloodAddress=_SfpsServiceCenterFloodAddress_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,6,1,1,1),_SfpsServiceCenterFloodAddress_Type())
sfpsServiceCenterFloodAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsServiceCenterFloodAddress.setStatus(_A)
_SfpsServiceCenterFloodMetric_Type=Integer32
_SfpsServiceCenterFloodMetric_Object=MibTableColumn
sfpsServiceCenterFloodMetric=_SfpsServiceCenterFloodMetric_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,6,1,1,2),_SfpsServiceCenterFloodMetric_Type())
sfpsServiceCenterFloodMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsServiceCenterFloodMetric.setStatus(_A)
_SfpsServiceCenterFloodName_Type=DisplayString
_SfpsServiceCenterFloodName_Object=MibTableColumn
sfpsServiceCenterFloodName=_SfpsServiceCenterFloodName_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,6,1,1,3),_SfpsServiceCenterFloodName_Type())
sfpsServiceCenterFloodName.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsServiceCenterFloodName.setStatus(_A)
class _SfpsServiceCenterFloodOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('kStatusRunning',1),('kStatusHalted',2),('kStatusPending',3),('kStatusFaulted',4),('kStatusNotStarted',5)))
_SfpsServiceCenterFloodOperStatus_Type.__name__=_D
_SfpsServiceCenterFloodOperStatus_Object=MibTableColumn
sfpsServiceCenterFloodOperStatus=_SfpsServiceCenterFloodOperStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,6,1,1,4),_SfpsServiceCenterFloodOperStatus_Type())
sfpsServiceCenterFloodOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsServiceCenterFloodOperStatus.setStatus(_A)
class _SfpsServiceCenterFloodAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),('disable',2),('enable',3)))
_SfpsServiceCenterFloodAdminStatus_Type.__name__=_D
_SfpsServiceCenterFloodAdminStatus_Object=MibTableColumn
sfpsServiceCenterFloodAdminStatus=_SfpsServiceCenterFloodAdminStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,6,1,1,5),_SfpsServiceCenterFloodAdminStatus_Type())
sfpsServiceCenterFloodAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsServiceCenterFloodAdminStatus.setStatus(_A)
_SfpsServiceCenterFloodStatusTime_Type=TimeTicks
_SfpsServiceCenterFloodStatusTime_Object=MibTableColumn
sfpsServiceCenterFloodStatusTime=_SfpsServiceCenterFloodStatusTime_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,6,1,1,6),_SfpsServiceCenterFloodStatusTime_Type())
sfpsServiceCenterFloodStatusTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsServiceCenterFloodStatusTime.setStatus(_A)
_SfpsServiceCenterFloodRequests_Type=Integer32
_SfpsServiceCenterFloodRequests_Object=MibTableColumn
sfpsServiceCenterFloodRequests=_SfpsServiceCenterFloodRequests_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,6,1,1,7),_SfpsServiceCenterFloodRequests_Type())
sfpsServiceCenterFloodRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsServiceCenterFloodRequests.setStatus(_A)
_SfpsServiceCenterFloodResponses_Type=Integer32
_SfpsServiceCenterFloodResponses_Object=MibTableColumn
sfpsServiceCenterFloodResponses=_SfpsServiceCenterFloodResponses_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,6,1,1,8),_SfpsServiceCenterFloodResponses_Type())
sfpsServiceCenterFloodResponses.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsServiceCenterFloodResponses.setStatus(_A)
_SfpsResolveCounterTable_Object=MibTable
sfpsResolveCounterTable=_SfpsResolveCounterTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,6,8,1))
if mibBuilder.loadTexts:sfpsResolveCounterTable.setStatus(_A)
_SfpsResolveCounterTableEntry_Object=MibTableRow
sfpsResolveCounterTableEntry=_SfpsResolveCounterTableEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,6,8,1,1))
sfpsResolveCounterTableEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:sfpsResolveCounterTableEntry.setStatus(_A)
_SfpsResolveCounterTableSource_Type=SfpsAddress
_SfpsResolveCounterTableSource_Object=MibTableColumn
sfpsResolveCounterTableSource=_SfpsResolveCounterTableSource_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,6,8,1,1,1),_SfpsResolveCounterTableSource_Type())
sfpsResolveCounterTableSource.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsResolveCounterTableSource.setStatus(_A)
_SfpsResolveCounterTableNumReq_Type=Integer32
_SfpsResolveCounterTableNumReq_Object=MibTableColumn
sfpsResolveCounterTableNumReq=_SfpsResolveCounterTableNumReq_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,6,8,1,1,2),_SfpsResolveCounterTableNumReq_Type())
sfpsResolveCounterTableNumReq.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsResolveCounterTableNumReq.setStatus(_A)
_SfpsResolveCounterTableNumRep_Type=Integer32
_SfpsResolveCounterTableNumRep_Object=MibTableColumn
sfpsResolveCounterTableNumRep=_SfpsResolveCounterTableNumRep_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,6,8,1,1,3),_SfpsResolveCounterTableNumRep_Type())
sfpsResolveCounterTableNumRep.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsResolveCounterTableNumRep.setStatus(_A)
_SfpsResolveCounterTableNumUnkRep_Type=Integer32
_SfpsResolveCounterTableNumUnkRep_Object=MibTableColumn
sfpsResolveCounterTableNumUnkRep=_SfpsResolveCounterTableNumUnkRep_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,6,8,1,1,4),_SfpsResolveCounterTableNumUnkRep_Type())
sfpsResolveCounterTableNumUnkRep.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsResolveCounterTableNumUnkRep.setStatus(_A)
_SfpsResolveCounterTableTicReq_Type=TimeTicks
_SfpsResolveCounterTableTicReq_Object=MibTableColumn
sfpsResolveCounterTableTicReq=_SfpsResolveCounterTableTicReq_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,6,8,1,1,5),_SfpsResolveCounterTableTicReq_Type())
sfpsResolveCounterTableTicReq.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsResolveCounterTableTicReq.setStatus(_A)
_SfpsResolveCounterTableTicRep_Type=TimeTicks
_SfpsResolveCounterTableTicRep_Object=MibTableColumn
sfpsResolveCounterTableTicRep=_SfpsResolveCounterTableTicRep_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,6,8,1,1,6),_SfpsResolveCounterTableTicRep_Type())
sfpsResolveCounterTableTicRep.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsResolveCounterTableTicRep.setStatus(_A)
_SfpsResolveCounterTableTicUnkRep_Type=TimeTicks
_SfpsResolveCounterTableTicUnkRep_Object=MibTableColumn
sfpsResolveCounterTableTicUnkRep=_SfpsResolveCounterTableTicUnkRep_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,6,8,1,1,7),_SfpsResolveCounterTableTicUnkRep_Type())
sfpsResolveCounterTableTicUnkRep.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsResolveCounterTableTicUnkRep.setStatus(_A)
_SfpsMobileUserTableAOType_Type=DisplayString
_SfpsMobileUserTableAOType_Object=MibScalar
sfpsMobileUserTableAOType=_SfpsMobileUserTableAOType_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,6,9,1,1),_SfpsMobileUserTableAOType_Type())
sfpsMobileUserTableAOType.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMobileUserTableAOType.setStatus(_A)
_SfpsMobileUserTableAOValue_Type=DisplayString
_SfpsMobileUserTableAOValue_Object=MibScalar
sfpsMobileUserTableAOValue=_SfpsMobileUserTableAOValue_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,6,9,1,2),_SfpsMobileUserTableAOValue_Type())
sfpsMobileUserTableAOValue.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMobileUserTableAOValue.setStatus(_A)
_SfpsMobileUserTableCount_Type=Integer32
_SfpsMobileUserTableCount_Object=MibScalar
sfpsMobileUserTableCount=_SfpsMobileUserTableCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,6,9,1,3),_SfpsMobileUserTableCount_Type())
sfpsMobileUserTableCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMobileUserTableCount.setStatus(_A)
_SfpsMobileUserTableNewSwitch_Type=SfpsAddress
_SfpsMobileUserTableNewSwitch_Object=MibScalar
sfpsMobileUserTableNewSwitch=_SfpsMobileUserTableNewSwitch_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,6,9,1,4),_SfpsMobileUserTableNewSwitch_Type())
sfpsMobileUserTableNewSwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMobileUserTableNewSwitch.setStatus(_A)
_SfpsMobileUserTableLastSeen_Type=TimeTicks
_SfpsMobileUserTableLastSeen_Object=MibScalar
sfpsMobileUserTableLastSeen=_SfpsMobileUserTableLastSeen_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,6,9,1,5),_SfpsMobileUserTableLastSeen_Type())
sfpsMobileUserTableLastSeen.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsMobileUserTableLastSeen.setStatus(_A)
_SfpsMobileUserTableFirstSceen_Type=TimeTicks
_SfpsMobileUserTableFirstSceen_Object=MibScalar
sfpsMobileUserTableFirstSceen=_SfpsMobileUserTableFirstSceen_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,6,9,1,6),_SfpsMobileUserTableFirstSceen_Type())
sfpsMobileUserTableFirstSceen.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsMobileUserTableFirstSceen.setStatus(_A)
_SfpsMobileUserTablePort_Type=Integer32
_SfpsMobileUserTablePort_Object=MibScalar
sfpsMobileUserTablePort=_SfpsMobileUserTablePort_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,6,9,1,7),_SfpsMobileUserTablePort_Type())
sfpsMobileUserTablePort.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsMobileUserTablePort.setStatus(_A)
_SfpsMobileUserResetReset_Type=Integer32
_SfpsMobileUserResetReset_Object=MibScalar
sfpsMobileUserResetReset=_SfpsMobileUserResetReset_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,6,9,2,1),_SfpsMobileUserResetReset_Type())
sfpsMobileUserResetReset.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsMobileUserResetReset.setStatus(_A)
_SfpsMobileUserResetCount_Type=Integer32
_SfpsMobileUserResetCount_Object=MibScalar
sfpsMobileUserResetCount=_SfpsMobileUserResetCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,6,9,2,2),_SfpsMobileUserResetCount_Type())
sfpsMobileUserResetCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMobileUserResetCount.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'HexInteger':HexInteger,'SfpsAddress':SfpsAddress,'sfpsServiceCenterFloodTable':sfpsServiceCenterFloodTable,'sfpsServiceCenterFloodEntry':sfpsServiceCenterFloodEntry,_F:sfpsServiceCenterFloodAddress,'sfpsServiceCenterFloodMetric':sfpsServiceCenterFloodMetric,'sfpsServiceCenterFloodName':sfpsServiceCenterFloodName,'sfpsServiceCenterFloodOperStatus':sfpsServiceCenterFloodOperStatus,'sfpsServiceCenterFloodAdminStatus':sfpsServiceCenterFloodAdminStatus,'sfpsServiceCenterFloodStatusTime':sfpsServiceCenterFloodStatusTime,'sfpsServiceCenterFloodRequests':sfpsServiceCenterFloodRequests,'sfpsServiceCenterFloodResponses':sfpsServiceCenterFloodResponses,'sfpsResolveCounterTable':sfpsResolveCounterTable,'sfpsResolveCounterTableEntry':sfpsResolveCounterTableEntry,_G:sfpsResolveCounterTableSource,'sfpsResolveCounterTableNumReq':sfpsResolveCounterTableNumReq,'sfpsResolveCounterTableNumRep':sfpsResolveCounterTableNumRep,'sfpsResolveCounterTableNumUnkRep':sfpsResolveCounterTableNumUnkRep,'sfpsResolveCounterTableTicReq':sfpsResolveCounterTableTicReq,'sfpsResolveCounterTableTicRep':sfpsResolveCounterTableTicRep,'sfpsResolveCounterTableTicUnkRep':sfpsResolveCounterTableTicUnkRep,'sfpsMobileUserTableAOType':sfpsMobileUserTableAOType,'sfpsMobileUserTableAOValue':sfpsMobileUserTableAOValue,'sfpsMobileUserTableCount':sfpsMobileUserTableCount,'sfpsMobileUserTableNewSwitch':sfpsMobileUserTableNewSwitch,'sfpsMobileUserTableLastSeen':sfpsMobileUserTableLastSeen,'sfpsMobileUserTableFirstSceen':sfpsMobileUserTableFirstSceen,'sfpsMobileUserTablePort':sfpsMobileUserTablePort,'sfpsMobileUserResetReset':sfpsMobileUserResetReset,'sfpsMobileUserResetCount':sfpsMobileUserResetCount})