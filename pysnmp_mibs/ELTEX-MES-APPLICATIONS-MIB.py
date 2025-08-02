_D='eltPingInetEntry'
_C='ELTEX-MES-APPLICATIONS-MIB'
_B='TruthValue'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltMes,=mibBuilder.importSymbols('ELTEX-MES','eltMes')
rsPingInetEntry,=mibBuilder.importSymbols('RADLAN-rndApplications','rsPingInetEntry')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_B)
eltMesApplicationsMIB=ModuleIdentity((1,3,6,1,4,1,35265,1,23,96))
if mibBuilder.loadTexts:eltMesApplicationsMIB.setRevisions(('2018-06-26 00:00',))
_EltMesApplicationsObjects_ObjectIdentity=ObjectIdentity
eltMesApplicationsObjects=_EltMesApplicationsObjects_ObjectIdentity((1,3,6,1,4,1,35265,1,23,96,1))
_EltMesApplicationsGlobals_ObjectIdentity=ObjectIdentity
eltMesApplicationsGlobals=_EltMesApplicationsGlobals_ObjectIdentity((1,3,6,1,4,1,35265,1,23,96,1,1))
_EltPingInetTable_Object=MibTable
eltPingInetTable=_EltPingInetTable_Object((1,3,6,1,4,1,35265,1,23,96,1,1,1))
if mibBuilder.loadTexts:eltPingInetTable.setStatus(_A)
_EltPingInetEntry_Object=MibTableRow
eltPingInetEntry=_EltPingInetEntry_Object((1,3,6,1,4,1,35265,1,23,96,1,1,1,1))
if mibBuilder.loadTexts:eltPingInetEntry.setStatus(_A)
class _EltPingInetDontFragment_Type(TruthValue):defaultValue=2
_EltPingInetDontFragment_Type.__name__=_B
_EltPingInetDontFragment_Object=MibTableColumn
eltPingInetDontFragment=_EltPingInetDontFragment_Object((1,3,6,1,4,1,35265,1,23,96,1,1,1,1,1),_EltPingInetDontFragment_Type())
eltPingInetDontFragment.setMaxAccess('read-write')
if mibBuilder.loadTexts:eltPingInetDontFragment.setStatus(_A)
rsPingInetEntry.registerAugmentions((_C,_D))
eltPingInetEntry.setIndexNames(*rsPingInetEntry.getIndexNames())
mibBuilder.exportSymbols(_C,**{'eltMesApplicationsMIB':eltMesApplicationsMIB,'eltMesApplicationsObjects':eltMesApplicationsObjects,'eltMesApplicationsGlobals':eltMesApplicationsGlobals,'eltPingInetTable':eltPingInetTable,_D:eltPingInetEntry,'eltPingInetDontFragment':eltPingInetDontFragment})