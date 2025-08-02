_G='read-write'
_F='noaction'
_E='rlsFlowDataSource'
_D='Dell-SFLOW-MIB'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rnd,=mibBuilder.importSymbols('Dell-MIB','rnd')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rlsFlowMib=ModuleIdentity((1,3,6,1,4,1,89,147))
if mibBuilder.loadTexts:rlsFlowMib.setRevisions(('2009-10-27 00:00',))
_RlsFlowStatisticsTable_Object=MibTable
rlsFlowStatisticsTable=_RlsFlowStatisticsTable_Object((1,3,6,1,4,1,89,147,1))
if mibBuilder.loadTexts:rlsFlowStatisticsTable.setStatus(_A)
_RlsFlowStatisticsEntry_Object=MibTableRow
rlsFlowStatisticsEntry=_RlsFlowStatisticsEntry_Object((1,3,6,1,4,1,89,147,1,1))
rlsFlowStatisticsEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:rlsFlowStatisticsEntry.setStatus(_A)
_RlsFlowDataSource_Type=ObjectIdentifier
_RlsFlowDataSource_Object=MibTableColumn
rlsFlowDataSource=_RlsFlowDataSource_Object((1,3,6,1,4,1,89,147,1,1,1),_RlsFlowDataSource_Type())
rlsFlowDataSource.setMaxAccess(_C)
if mibBuilder.loadTexts:rlsFlowDataSource.setStatus(_A)
_RlsFlowStatisticsSampledPackets_Type=Counter32
_RlsFlowStatisticsSampledPackets_Object=MibTableColumn
rlsFlowStatisticsSampledPackets=_RlsFlowStatisticsSampledPackets_Object((1,3,6,1,4,1,89,147,1,1,2),_RlsFlowStatisticsSampledPackets_Type())
rlsFlowStatisticsSampledPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:rlsFlowStatisticsSampledPackets.setStatus(_A)
_RlsFlowStatisticsDatagramSent_Type=Counter32
_RlsFlowStatisticsDatagramSent_Object=MibTableColumn
rlsFlowStatisticsDatagramSent=_RlsFlowStatisticsDatagramSent_Object((1,3,6,1,4,1,89,147,1,1,3),_RlsFlowStatisticsDatagramSent_Type())
rlsFlowStatisticsDatagramSent.setMaxAccess(_C)
if mibBuilder.loadTexts:rlsFlowStatisticsDatagramSent.setStatus(_A)
class _RlsFlowStatisticsAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),('clear',2)))
_RlsFlowStatisticsAction_Type.__name__=_B
_RlsFlowStatisticsAction_Object=MibTableColumn
rlsFlowStatisticsAction=_RlsFlowStatisticsAction_Object((1,3,6,1,4,1,89,147,1,1,4),_RlsFlowStatisticsAction_Type())
rlsFlowStatisticsAction.setMaxAccess(_G)
if mibBuilder.loadTexts:rlsFlowStatisticsAction.setStatus(_A)
class _RlsFlowStatisticsReset_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),('clear',2)))
_RlsFlowStatisticsReset_Type.__name__=_B
_RlsFlowStatisticsReset_Object=MibScalar
rlsFlowStatisticsReset=_RlsFlowStatisticsReset_Object((1,3,6,1,4,1,89,147,2),_RlsFlowStatisticsReset_Type())
rlsFlowStatisticsReset.setMaxAccess(_G)
if mibBuilder.loadTexts:rlsFlowStatisticsReset.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'rlsFlowMib':rlsFlowMib,'rlsFlowStatisticsTable':rlsFlowStatisticsTable,'rlsFlowStatisticsEntry':rlsFlowStatisticsEntry,_E:rlsFlowDataSource,'rlsFlowStatisticsSampledPackets':rlsFlowStatisticsSampledPackets,'rlsFlowStatisticsDatagramSent':rlsFlowStatisticsDatagramSent,'rlsFlowStatisticsAction':rlsFlowStatisticsAction,'rlsFlowStatisticsReset':rlsFlowStatisticsReset})