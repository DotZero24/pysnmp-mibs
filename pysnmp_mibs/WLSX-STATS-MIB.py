_D='wlsxStatsIndex'
_C='WLSX-STATS-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
wlsxEnterpriseMibModules,=mibBuilder.importSymbols('ARUBA-MIB','wlsxEnterpriseMibModules')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,snmpModules=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','snmpModules')
DisplayString,MacAddress,PhysAddress,RowStatus,StorageType,TAddress,TDomain,TextualConvention,TestAndIncr,TimeInterval,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','StorageType','TAddress','TDomain','TextualConvention','TestAndIncr','TimeInterval','TruthValue')
wlsxStatsMIB=ModuleIdentity((1,3,6,1,4,1,14823,2,2,1,15))
if mibBuilder.loadTexts:wlsxStatsMIB.setRevisions(('2020-08-14 17:45',))
_WlsxStatsOpGroup_ObjectIdentity=ObjectIdentity
wlsxStatsOpGroup=_WlsxStatsOpGroup_ObjectIdentity((1,3,6,1,4,1,14823,2,2,1,15,1))
_WlsxStatsRequestTable_Object=MibTable
wlsxStatsRequestTable=_WlsxStatsRequestTable_Object((1,3,6,1,4,1,14823,2,2,1,15,1,1))
if mibBuilder.loadTexts:wlsxStatsRequestTable.setStatus(_A)
_WlsxStatsRequestEntry_Object=MibTableRow
wlsxStatsRequestEntry=_WlsxStatsRequestEntry_Object((1,3,6,1,4,1,14823,2,2,1,15,1,1,1))
wlsxStatsRequestEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:wlsxStatsRequestEntry.setStatus(_A)
_WlsxStatsIndex_Type=Integer32
_WlsxStatsIndex_Object=MibTableColumn
wlsxStatsIndex=_WlsxStatsIndex_Object((1,3,6,1,4,1,14823,2,2,1,15,1,1,1,1),_WlsxStatsIndex_Type())
wlsxStatsIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:wlsxStatsIndex.setStatus(_A)
_WlsxStatsReqType_Type=Integer32
_WlsxStatsReqType_Object=MibTableColumn
wlsxStatsReqType=_WlsxStatsReqType_Object((1,3,6,1,4,1,14823,2,2,1,15,1,1,1,2),_WlsxStatsReqType_Type())
wlsxStatsReqType.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxStatsReqType.setStatus(_A)
_WlsxStatsInterval_Type=Integer32
_WlsxStatsInterval_Object=MibTableColumn
wlsxStatsInterval=_WlsxStatsInterval_Object((1,3,6,1,4,1,14823,2,2,1,15,1,1,1,3),_WlsxStatsInterval_Type())
wlsxStatsInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxStatsInterval.setStatus(_A)
_WlsxStatsCookie_Type=DisplayString
_WlsxStatsCookie_Object=MibTableColumn
wlsxStatsCookie=_WlsxStatsCookie_Object((1,3,6,1,4,1,14823,2,2,1,15,1,1,1,4),_WlsxStatsCookie_Type())
wlsxStatsCookie.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxStatsCookie.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'wlsxStatsMIB':wlsxStatsMIB,'wlsxStatsOpGroup':wlsxStatsOpGroup,'wlsxStatsRequestTable':wlsxStatsRequestTable,'wlsxStatsRequestEntry':wlsxStatsRequestEntry,_D:wlsxStatsIndex,'wlsxStatsReqType':wlsxStatsReqType,'wlsxStatsInterval':wlsxStatsInterval,'wlsxStatsCookie':wlsxStatsCookie})