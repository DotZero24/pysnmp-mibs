_E='sfpsServiceCenterConnectAddress'
_D='CTRON-SFPS-CONN-MIB'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
sfpsServiceCenter,=mibBuilder.importSymbols('CTRON-SFPS-INCLUDE-MIB','sfpsServiceCenter')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class HexInteger(Integer32):0
_SfpsServiceCenterConnectTable_Object=MibTable
sfpsServiceCenterConnectTable=_SfpsServiceCenterConnectTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,4))
if mibBuilder.loadTexts:sfpsServiceCenterConnectTable.setStatus(_A)
_SfpsServiceCenterConnectEntry_Object=MibTableRow
sfpsServiceCenterConnectEntry=_SfpsServiceCenterConnectEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,4,1))
sfpsServiceCenterConnectEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:sfpsServiceCenterConnectEntry.setStatus(_A)
_SfpsServiceCenterConnectAddress_Type=HexInteger
_SfpsServiceCenterConnectAddress_Object=MibTableColumn
sfpsServiceCenterConnectAddress=_SfpsServiceCenterConnectAddress_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,4,1,1),_SfpsServiceCenterConnectAddress_Type())
sfpsServiceCenterConnectAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsServiceCenterConnectAddress.setStatus(_A)
_SfpsServiceCenterConnectMetric_Type=Integer32
_SfpsServiceCenterConnectMetric_Object=MibTableColumn
sfpsServiceCenterConnectMetric=_SfpsServiceCenterConnectMetric_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,4,1,2),_SfpsServiceCenterConnectMetric_Type())
sfpsServiceCenterConnectMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsServiceCenterConnectMetric.setStatus(_A)
_SfpsServiceCenterConnectName_Type=DisplayString
_SfpsServiceCenterConnectName_Object=MibTableColumn
sfpsServiceCenterConnectName=_SfpsServiceCenterConnectName_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,4,1,3),_SfpsServiceCenterConnectName_Type())
sfpsServiceCenterConnectName.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsServiceCenterConnectName.setStatus(_A)
class _SfpsServiceCenterConnectOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('kStatusRunning',1),('kStatusHalted',2),('kStatusPending',3),('kStatusFaulted',4),('kStatusNotStarted',5)))
_SfpsServiceCenterConnectOperStatus_Type.__name__=_C
_SfpsServiceCenterConnectOperStatus_Object=MibTableColumn
sfpsServiceCenterConnectOperStatus=_SfpsServiceCenterConnectOperStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,4,1,4),_SfpsServiceCenterConnectOperStatus_Type())
sfpsServiceCenterConnectOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsServiceCenterConnectOperStatus.setStatus(_A)
class _SfpsServiceCenterConnectAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),('disable',2),('enable',3)))
_SfpsServiceCenterConnectAdminStatus_Type.__name__=_C
_SfpsServiceCenterConnectAdminStatus_Object=MibTableColumn
sfpsServiceCenterConnectAdminStatus=_SfpsServiceCenterConnectAdminStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,4,1,5),_SfpsServiceCenterConnectAdminStatus_Type())
sfpsServiceCenterConnectAdminStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:sfpsServiceCenterConnectAdminStatus.setStatus(_A)
_SfpsServiceCenterConnectStatusTime_Type=TimeTicks
_SfpsServiceCenterConnectStatusTime_Object=MibTableColumn
sfpsServiceCenterConnectStatusTime=_SfpsServiceCenterConnectStatusTime_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,4,1,6),_SfpsServiceCenterConnectStatusTime_Type())
sfpsServiceCenterConnectStatusTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsServiceCenterConnectStatusTime.setStatus(_A)
_SfpsServiceCenterConnectRequests_Type=Integer32
_SfpsServiceCenterConnectRequests_Object=MibTableColumn
sfpsServiceCenterConnectRequests=_SfpsServiceCenterConnectRequests_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,4,1,7),_SfpsServiceCenterConnectRequests_Type())
sfpsServiceCenterConnectRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsServiceCenterConnectRequests.setStatus(_A)
_SfpsServiceCenterConnectResponses_Type=Integer32
_SfpsServiceCenterConnectResponses_Object=MibTableColumn
sfpsServiceCenterConnectResponses=_SfpsServiceCenterConnectResponses_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,4,1,8),_SfpsServiceCenterConnectResponses_Type())
sfpsServiceCenterConnectResponses.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsServiceCenterConnectResponses.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'HexInteger':HexInteger,'sfpsServiceCenterConnectTable':sfpsServiceCenterConnectTable,'sfpsServiceCenterConnectEntry':sfpsServiceCenterConnectEntry,_E:sfpsServiceCenterConnectAddress,'sfpsServiceCenterConnectMetric':sfpsServiceCenterConnectMetric,'sfpsServiceCenterConnectName':sfpsServiceCenterConnectName,'sfpsServiceCenterConnectOperStatus':sfpsServiceCenterConnectOperStatus,'sfpsServiceCenterConnectAdminStatus':sfpsServiceCenterConnectAdminStatus,'sfpsServiceCenterConnectStatusTime':sfpsServiceCenterConnectStatusTime,'sfpsServiceCenterConnectRequests':sfpsServiceCenterConnectRequests,'sfpsServiceCenterConnectResponses':sfpsServiceCenterConnectResponses})