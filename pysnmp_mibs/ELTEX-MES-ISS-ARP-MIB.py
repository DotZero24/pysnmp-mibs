_G='Integer32'
_F='read-write'
_E='TruthValue'
_D='ifIndex'
_C='IF-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltMesIss,=mibBuilder.importSymbols('ELTEX-MES-ISS-MIB','eltMesIss')
ifIndex,=mibBuilder.importSymbols(_C,_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_E)
eltMesIssArpMIB=ModuleIdentity((1,3,6,1,4,1,35265,1,139,26))
if mibBuilder.loadTexts:eltMesIssArpMIB.setRevisions(('1970-01-01 00:00','2021-03-09 00:00'))
_EltMesIssArpObjects_ObjectIdentity=ObjectIdentity
eltMesIssArpObjects=_EltMesIssArpObjects_ObjectIdentity((1,3,6,1,4,1,35265,1,139,26,1))
_EltMesIssArpInterfaceConfigs_ObjectIdentity=ObjectIdentity
eltMesIssArpInterfaceConfigs=_EltMesIssArpInterfaceConfigs_ObjectIdentity((1,3,6,1,4,1,35265,1,139,26,1,1))
_EltMesIssArpInterfaceTable_Object=MibTable
eltMesIssArpInterfaceTable=_EltMesIssArpInterfaceTable_Object((1,3,6,1,4,1,35265,1,139,26,1,1,1))
if mibBuilder.loadTexts:eltMesIssArpInterfaceTable.setStatus(_A)
_EltMesIssArpInterfaceEntry_Object=MibTableRow
eltMesIssArpInterfaceEntry=_EltMesIssArpInterfaceEntry_Object((1,3,6,1,4,1,35265,1,139,26,1,1,1,1))
eltMesIssArpInterfaceEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:eltMesIssArpInterfaceEntry.setStatus(_A)
class _EltMesIssArpGratuitousPeriodicEnable_Type(TruthValue):defaultValue=1
_EltMesIssArpGratuitousPeriodicEnable_Type.__name__=_E
_EltMesIssArpGratuitousPeriodicEnable_Object=MibTableColumn
eltMesIssArpGratuitousPeriodicEnable=_EltMesIssArpGratuitousPeriodicEnable_Object((1,3,6,1,4,1,35265,1,139,26,1,1,1,1,1),_EltMesIssArpGratuitousPeriodicEnable_Type())
eltMesIssArpGratuitousPeriodicEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:eltMesIssArpGratuitousPeriodicEnable.setStatus(_A)
_EltMesIssArpGlobals_ObjectIdentity=ObjectIdentity
eltMesIssArpGlobals=_EltMesIssArpGlobals_ObjectIdentity((1,3,6,1,4,1,35265,1,139,26,1,2))
class _EltMesIssArpGratuitousInterval_Type(Integer32):defaultValue=150;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(15,86400))
_EltMesIssArpGratuitousInterval_Type.__name__=_G
_EltMesIssArpGratuitousInterval_Object=MibScalar
eltMesIssArpGratuitousInterval=_EltMesIssArpGratuitousInterval_Object((1,3,6,1,4,1,35265,1,139,26,1,2,1),_EltMesIssArpGratuitousInterval_Type())
eltMesIssArpGratuitousInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:eltMesIssArpGratuitousInterval.setStatus(_A)
_EltMesIssArpInspection_ObjectIdentity=ObjectIdentity
eltMesIssArpInspection=_EltMesIssArpInspection_ObjectIdentity((1,3,6,1,4,1,35265,1,139,26,1,3))
_EltMesIssArpInspectionStats_ObjectIdentity=ObjectIdentity
eltMesIssArpInspectionStats=_EltMesIssArpInspectionStats_ObjectIdentity((1,3,6,1,4,1,35265,1,139,26,1,3,1))
_EltMesIssArpInspectionIfStatsTable_Object=MibTable
eltMesIssArpInspectionIfStatsTable=_EltMesIssArpInspectionIfStatsTable_Object((1,3,6,1,4,1,35265,1,139,26,1,3,1,1))
if mibBuilder.loadTexts:eltMesIssArpInspectionIfStatsTable.setStatus(_A)
_EltMesIssArpInspectionIfStatsEntry_Object=MibTableRow
eltMesIssArpInspectionIfStatsEntry=_EltMesIssArpInspectionIfStatsEntry_Object((1,3,6,1,4,1,35265,1,139,26,1,3,1,1,1))
eltMesIssArpInspectionIfStatsEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:eltMesIssArpInspectionIfStatsEntry.setStatus(_A)
_EltMesIssArpInspectionIfForwardedPackets_Type=Integer32
_EltMesIssArpInspectionIfForwardedPackets_Object=MibTableColumn
eltMesIssArpInspectionIfForwardedPackets=_EltMesIssArpInspectionIfForwardedPackets_Object((1,3,6,1,4,1,35265,1,139,26,1,3,1,1,1,1),_EltMesIssArpInspectionIfForwardedPackets_Type())
eltMesIssArpInspectionIfForwardedPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssArpInspectionIfForwardedPackets.setStatus(_A)
_EltMesIssArpInspectionIfDroppedPackets_Type=Integer32
_EltMesIssArpInspectionIfDroppedPackets_Object=MibTableColumn
eltMesIssArpInspectionIfDroppedPackets=_EltMesIssArpInspectionIfDroppedPackets_Object((1,3,6,1,4,1,35265,1,139,26,1,3,1,1,1,2),_EltMesIssArpInspectionIfDroppedPackets_Type())
eltMesIssArpInspectionIfDroppedPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssArpInspectionIfDroppedPackets.setStatus(_A)
_EltMesIssArpInspectionIfIPValidFailures_Type=Integer32
_EltMesIssArpInspectionIfIPValidFailures_Object=MibTableColumn
eltMesIssArpInspectionIfIPValidFailures=_EltMesIssArpInspectionIfIPValidFailures_Object((1,3,6,1,4,1,35265,1,139,26,1,3,1,1,1,3),_EltMesIssArpInspectionIfIPValidFailures_Type())
eltMesIssArpInspectionIfIPValidFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssArpInspectionIfIPValidFailures.setStatus(_A)
_EltMesIssArpInspectionIfDestMacFailures_Type=Integer32
_EltMesIssArpInspectionIfDestMacFailures_Object=MibTableColumn
eltMesIssArpInspectionIfDestMacFailures=_EltMesIssArpInspectionIfDestMacFailures_Object((1,3,6,1,4,1,35265,1,139,26,1,3,1,1,1,4),_EltMesIssArpInspectionIfDestMacFailures_Type())
eltMesIssArpInspectionIfDestMacFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssArpInspectionIfDestMacFailures.setStatus(_A)
_EltMesIssArpInspectionIfSrcMacFailures_Type=Integer32
_EltMesIssArpInspectionIfSrcMacFailures_Object=MibTableColumn
eltMesIssArpInspectionIfSrcMacFailures=_EltMesIssArpInspectionIfSrcMacFailures_Object((1,3,6,1,4,1,35265,1,139,26,1,3,1,1,1,5),_EltMesIssArpInspectionIfSrcMacFailures_Type())
eltMesIssArpInspectionIfSrcMacFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssArpInspectionIfSrcMacFailures.setStatus(_A)
class _EltMesIssArpInsectionIfStatsClear_Type(TruthValue):defaultValue=2
_EltMesIssArpInsectionIfStatsClear_Type.__name__=_E
_EltMesIssArpInsectionIfStatsClear_Object=MibTableColumn
eltMesIssArpInsectionIfStatsClear=_EltMesIssArpInsectionIfStatsClear_Object((1,3,6,1,4,1,35265,1,139,26,1,3,1,1,1,6),_EltMesIssArpInsectionIfStatsClear_Type())
eltMesIssArpInsectionIfStatsClear.setMaxAccess(_F)
if mibBuilder.loadTexts:eltMesIssArpInsectionIfStatsClear.setStatus(_A)
mibBuilder.exportSymbols('ELTEX-MES-ISS-ARP-MIB',**{'eltMesIssArpMIB':eltMesIssArpMIB,'eltMesIssArpObjects':eltMesIssArpObjects,'eltMesIssArpInterfaceConfigs':eltMesIssArpInterfaceConfigs,'eltMesIssArpInterfaceTable':eltMesIssArpInterfaceTable,'eltMesIssArpInterfaceEntry':eltMesIssArpInterfaceEntry,'eltMesIssArpGratuitousPeriodicEnable':eltMesIssArpGratuitousPeriodicEnable,'eltMesIssArpGlobals':eltMesIssArpGlobals,'eltMesIssArpGratuitousInterval':eltMesIssArpGratuitousInterval,'eltMesIssArpInspection':eltMesIssArpInspection,'eltMesIssArpInspectionStats':eltMesIssArpInspectionStats,'eltMesIssArpInspectionIfStatsTable':eltMesIssArpInspectionIfStatsTable,'eltMesIssArpInspectionIfStatsEntry':eltMesIssArpInspectionIfStatsEntry,'eltMesIssArpInspectionIfForwardedPackets':eltMesIssArpInspectionIfForwardedPackets,'eltMesIssArpInspectionIfDroppedPackets':eltMesIssArpInspectionIfDroppedPackets,'eltMesIssArpInspectionIfIPValidFailures':eltMesIssArpInspectionIfIPValidFailures,'eltMesIssArpInspectionIfDestMacFailures':eltMesIssArpInspectionIfDestMacFailures,'eltMesIssArpInspectionIfSrcMacFailures':eltMesIssArpInspectionIfSrcMacFailures,'eltMesIssArpInsectionIfStatsClear':eltMesIssArpInsectionIfStatsClear})