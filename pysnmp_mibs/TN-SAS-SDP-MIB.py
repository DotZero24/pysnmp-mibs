_F='sdpBindBaseStatsExtnEntry'
_E='sdpBindExtnEntry'
_D='read-only'
_C='TruthValue'
_B='TN-SAS-SDP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_C)
sdpBindBaseStatsEntry,sdpBindEntry=mibBuilder.importSymbols('TN-SDP-MIB','sdpBindBaseStatsEntry','sdpBindEntry')
tnSASModules,tnSASObjs=mibBuilder.importSymbols('TROPIC-GLOBAL-REG','tnSASModules','tnSASObjs')
tnSASServicesSdpMIBModule=ModuleIdentity((1,3,6,1,4,1,7483,7,2,1,1,12))
if mibBuilder.loadTexts:tnSASServicesSdpMIBModule.setRevisions(('2015-07-30 00:00','2007-10-01 00:00'))
_TnSASSdpObjs_ObjectIdentity=ObjectIdentity
tnSASSdpObjs=_TnSASSdpObjs_ObjectIdentity((1,3,6,1,4,1,7483,7,2,2,2,12))
_SdpBindExtnTable_Object=MibTable
sdpBindExtnTable=_SdpBindExtnTable_Object((1,3,6,1,4,1,7483,7,2,2,2,12,4))
if mibBuilder.loadTexts:sdpBindExtnTable.setStatus(_A)
_SdpBindExtnEntry_Object=MibTableRow
sdpBindExtnEntry=_SdpBindExtnEntry_Object((1,3,6,1,4,1,7483,7,2,2,2,12,4,1))
if mibBuilder.loadTexts:sdpBindExtnEntry.setStatus(_A)
class _SdpBindIngressExtraVlanTagDropCount_Type(TruthValue):defaultValue=2
_SdpBindIngressExtraVlanTagDropCount_Type.__name__=_C
_SdpBindIngressExtraVlanTagDropCount_Object=MibTableColumn
sdpBindIngressExtraVlanTagDropCount=_SdpBindIngressExtraVlanTagDropCount_Object((1,3,6,1,4,1,7483,7,2,2,2,12,4,1,1),_SdpBindIngressExtraVlanTagDropCount_Type())
sdpBindIngressExtraVlanTagDropCount.setMaxAccess('read-create')
if mibBuilder.loadTexts:sdpBindIngressExtraVlanTagDropCount.setStatus(_A)
_SdpBindBaseStatsExtnTable_Object=MibTable
sdpBindBaseStatsExtnTable=_SdpBindBaseStatsExtnTable_Object((1,3,6,1,4,1,7483,7,2,2,2,12,5))
if mibBuilder.loadTexts:sdpBindBaseStatsExtnTable.setStatus(_A)
_SdpBindBaseStatsExtnEntry_Object=MibTableRow
sdpBindBaseStatsExtnEntry=_SdpBindBaseStatsExtnEntry_Object((1,3,6,1,4,1,7483,7,2,2,2,12,5,1))
if mibBuilder.loadTexts:sdpBindBaseStatsExtnEntry.setStatus(_A)
_SdpBindIngressExtraVlanTagDroppedPackets_Type=Counter64
_SdpBindIngressExtraVlanTagDroppedPackets_Object=MibTableColumn
sdpBindIngressExtraVlanTagDroppedPackets=_SdpBindIngressExtraVlanTagDroppedPackets_Object((1,3,6,1,4,1,7483,7,2,2,2,12,5,1,1),_SdpBindIngressExtraVlanTagDroppedPackets_Type())
sdpBindIngressExtraVlanTagDroppedPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:sdpBindIngressExtraVlanTagDroppedPackets.setStatus(_A)
_SdpBindIngressExtraVlanTagDroppedOctets_Type=Counter64
_SdpBindIngressExtraVlanTagDroppedOctets_Object=MibTableColumn
sdpBindIngressExtraVlanTagDroppedOctets=_SdpBindIngressExtraVlanTagDroppedOctets_Object((1,3,6,1,4,1,7483,7,2,2,2,12,5,1,2),_SdpBindIngressExtraVlanTagDroppedOctets_Type())
sdpBindIngressExtraVlanTagDroppedOctets.setMaxAccess(_D)
if mibBuilder.loadTexts:sdpBindIngressExtraVlanTagDroppedOctets.setStatus(_A)
sdpBindEntry.registerAugmentions((_B,_E))
sdpBindExtnEntry.setIndexNames(*sdpBindEntry.getIndexNames())
sdpBindBaseStatsEntry.registerAugmentions((_B,_F))
sdpBindBaseStatsExtnEntry.setIndexNames(*sdpBindBaseStatsEntry.getIndexNames())
mibBuilder.exportSymbols(_B,**{'tnSASServicesSdpMIBModule':tnSASServicesSdpMIBModule,'tnSASSdpObjs':tnSASSdpObjs,'sdpBindExtnTable':sdpBindExtnTable,_E:sdpBindExtnEntry,'sdpBindIngressExtraVlanTagDropCount':sdpBindIngressExtraVlanTagDropCount,'sdpBindBaseStatsExtnTable':sdpBindBaseStatsExtnTable,_F:sdpBindBaseStatsExtnEntry,'sdpBindIngressExtraVlanTagDroppedPackets':sdpBindIngressExtraVlanTagDroppedPackets,'sdpBindIngressExtraVlanTagDroppedOctets':sdpBindIngressExtraVlanTagDroppedOctets})