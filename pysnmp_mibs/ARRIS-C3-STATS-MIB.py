_E='dcxCmtsServiceEntry'
_D='dcxUsStatsIfIndex'
_C='ARRIS-C3-STATS-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cmtsC3,=mibBuilder.importSymbols('ARRIS-MIB','cmtsC3')
docsIfCmtsServiceEntry,=mibBuilder.importSymbols('DOCS-IF-MIB','docsIfCmtsServiceEntry')
InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero','ifIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
cmtsC3StatsMIB=ModuleIdentity((1,3,6,1,4,1,4115,1,4,3,1))
_DcxUpstreamStatsObjects_ObjectIdentity=ObjectIdentity
dcxUpstreamStatsObjects=_DcxUpstreamStatsObjects_ObjectIdentity((1,3,6,1,4,1,4115,1,4,3,1,1))
_DcxUpstreamStatsTable_Object=MibTable
dcxUpstreamStatsTable=_DcxUpstreamStatsTable_Object((1,3,6,1,4,1,4115,1,4,3,1,1,1))
if mibBuilder.loadTexts:dcxUpstreamStatsTable.setStatus(_A)
_DcxUpstreamStatsEntry_Object=MibTableRow
dcxUpstreamStatsEntry=_DcxUpstreamStatsEntry_Object((1,3,6,1,4,1,4115,1,4,3,1,1,1,1))
dcxUpstreamStatsEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:dcxUpstreamStatsEntry.setStatus(_A)
_DcxUsStatsOther_Type=Counter32
_DcxUsStatsOther_Object=MibTableColumn
dcxUsStatsOther=_DcxUsStatsOther_Object((1,3,6,1,4,1,4115,1,4,3,1,1,1,1,1),_DcxUsStatsOther_Type())
dcxUsStatsOther.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxUsStatsOther.setStatus(_A)
_DcxUsStatsRanging_Type=Counter32
_DcxUsStatsRanging_Object=MibTableColumn
dcxUsStatsRanging=_DcxUsStatsRanging_Object((1,3,6,1,4,1,4115,1,4,3,1,1,1,1,2),_DcxUsStatsRanging_Type())
dcxUsStatsRanging.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxUsStatsRanging.setStatus(_A)
_DcxUsStatsRngAborted_Type=Counter32
_DcxUsStatsRngAborted_Object=MibTableColumn
dcxUsStatsRngAborted=_DcxUsStatsRngAborted_Object((1,3,6,1,4,1,4115,1,4,3,1,1,1,1,3),_DcxUsStatsRngAborted_Type())
dcxUsStatsRngAborted.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxUsStatsRngAborted.setStatus(_A)
_DcxUsStatsRngComplete_Type=Counter32
_DcxUsStatsRngComplete_Object=MibTableColumn
dcxUsStatsRngComplete=_DcxUsStatsRngComplete_Object((1,3,6,1,4,1,4115,1,4,3,1,1,1,1,4),_DcxUsStatsRngComplete_Type())
dcxUsStatsRngComplete.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxUsStatsRngComplete.setStatus(_A)
_DcxUsStatsIpComplete_Type=Counter32
_DcxUsStatsIpComplete_Object=MibTableColumn
dcxUsStatsIpComplete=_DcxUsStatsIpComplete_Object((1,3,6,1,4,1,4115,1,4,3,1,1,1,1,5),_DcxUsStatsIpComplete_Type())
dcxUsStatsIpComplete.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxUsStatsIpComplete.setStatus(_A)
_DcxUsStatsRegComplete_Type=Counter32
_DcxUsStatsRegComplete_Object=MibTableColumn
dcxUsStatsRegComplete=_DcxUsStatsRegComplete_Object((1,3,6,1,4,1,4115,1,4,3,1,1,1,1,6),_DcxUsStatsRegComplete_Type())
dcxUsStatsRegComplete.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxUsStatsRegComplete.setStatus(_A)
_DcxUsStatsAccessDenied_Type=Counter32
_DcxUsStatsAccessDenied_Object=MibTableColumn
dcxUsStatsAccessDenied=_DcxUsStatsAccessDenied_Object((1,3,6,1,4,1,4115,1,4,3,1,1,1,1,7),_DcxUsStatsAccessDenied_Type())
dcxUsStatsAccessDenied.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxUsStatsAccessDenied.setStatus(_A)
_DcxUsStatsIfIndex_Type=InterfaceIndexOrZero
_DcxUsStatsIfIndex_Object=MibTableColumn
dcxUsStatsIfIndex=_DcxUsStatsIfIndex_Object((1,3,6,1,4,1,4115,1,4,3,1,1,1,1,8),_DcxUsStatsIfIndex_Type())
dcxUsStatsIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxUsStatsIfIndex.setStatus(_A)
_DcxCmtsServiceStatsObjects_ObjectIdentity=ObjectIdentity
dcxCmtsServiceStatsObjects=_DcxCmtsServiceStatsObjects_ObjectIdentity((1,3,6,1,4,1,4115,1,4,3,1,2))
_DcxCmtsServiceTable_Object=MibTable
dcxCmtsServiceTable=_DcxCmtsServiceTable_Object((1,3,6,1,4,1,4115,1,4,3,1,2,1))
if mibBuilder.loadTexts:dcxCmtsServiceTable.setStatus(_A)
_DcxCmtsServiceEntry_Object=MibTableRow
dcxCmtsServiceEntry=_DcxCmtsServiceEntry_Object((1,3,6,1,4,1,4115,1,4,3,1,2,1,1))
if mibBuilder.loadTexts:dcxCmtsServiceEntry.setStatus(_A)
_DcxCmtsServiceOutOctets_Type=Counter32
_DcxCmtsServiceOutOctets_Object=MibTableColumn
dcxCmtsServiceOutOctets=_DcxCmtsServiceOutOctets_Object((1,3,6,1,4,1,4115,1,4,3,1,2,1,1,1),_DcxCmtsServiceOutOctets_Type())
dcxCmtsServiceOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxCmtsServiceOutOctets.setStatus(_A)
_DcxCmtsServiceOutPackets_Type=Counter32
_DcxCmtsServiceOutPackets_Object=MibTableColumn
dcxCmtsServiceOutPackets=_DcxCmtsServiceOutPackets_Object((1,3,6,1,4,1,4115,1,4,3,1,2,1,1,2),_DcxCmtsServiceOutPackets_Type())
dcxCmtsServiceOutPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxCmtsServiceOutPackets.setStatus(_A)
_CdxCmtsServiceUpBWExcessReqs_Type=Counter32
_CdxCmtsServiceUpBWExcessReqs_Object=MibTableColumn
cdxCmtsServiceUpBWExcessReqs=_CdxCmtsServiceUpBWExcessReqs_Object((1,3,6,1,4,1,4115,1,4,3,1,2,1,1,3),_CdxCmtsServiceUpBWExcessReqs_Type())
cdxCmtsServiceUpBWExcessReqs.setMaxAccess(_B)
if mibBuilder.loadTexts:cdxCmtsServiceUpBWExcessReqs.setStatus(_A)
_CdxCmtsServiceDownBWExcessPkts_Type=Counter32
_CdxCmtsServiceDownBWExcessPkts_Object=MibTableColumn
cdxCmtsServiceDownBWExcessPkts=_CdxCmtsServiceDownBWExcessPkts_Object((1,3,6,1,4,1,4115,1,4,3,1,2,1,1,4),_CdxCmtsServiceDownBWExcessPkts_Type())
cdxCmtsServiceDownBWExcessPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cdxCmtsServiceDownBWExcessPkts.setStatus(_A)
docsIfCmtsServiceEntry.registerAugmentions((_C,_E))
dcxCmtsServiceEntry.setIndexNames(*docsIfCmtsServiceEntry.getIndexNames())
mibBuilder.exportSymbols(_C,**{'cmtsC3StatsMIB':cmtsC3StatsMIB,'dcxUpstreamStatsObjects':dcxUpstreamStatsObjects,'dcxUpstreamStatsTable':dcxUpstreamStatsTable,'dcxUpstreamStatsEntry':dcxUpstreamStatsEntry,'dcxUsStatsOther':dcxUsStatsOther,'dcxUsStatsRanging':dcxUsStatsRanging,'dcxUsStatsRngAborted':dcxUsStatsRngAborted,'dcxUsStatsRngComplete':dcxUsStatsRngComplete,'dcxUsStatsIpComplete':dcxUsStatsIpComplete,'dcxUsStatsRegComplete':dcxUsStatsRegComplete,'dcxUsStatsAccessDenied':dcxUsStatsAccessDenied,_D:dcxUsStatsIfIndex,'dcxCmtsServiceStatsObjects':dcxCmtsServiceStatsObjects,'dcxCmtsServiceTable':dcxCmtsServiceTable,_E:dcxCmtsServiceEntry,'dcxCmtsServiceOutOctets':dcxCmtsServiceOutOctets,'dcxCmtsServiceOutPackets':dcxCmtsServiceOutPackets,'cdxCmtsServiceUpBWExcessReqs':cdxCmtsServiceUpBWExcessReqs,'cdxCmtsServiceDownBWExcessPkts':cdxCmtsServiceDownBWExcessPkts})