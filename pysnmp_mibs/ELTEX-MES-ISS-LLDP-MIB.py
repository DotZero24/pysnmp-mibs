_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltMesIss,=mibBuilder.importSymbols('ELTEX-MES-ISS-MIB','eltMesIss')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
eltMesIssLldpMIB=ModuleIdentity((1,3,6,1,4,1,35265,1,139,10))
if mibBuilder.loadTexts:eltMesIssLldpMIB.setRevisions(('2019-02-12 00:00',))
_EltMesIssLldpObjects_ObjectIdentity=ObjectIdentity
eltMesIssLldpObjects=_EltMesIssLldpObjects_ObjectIdentity((1,3,6,1,4,1,35265,1,139,10,1))
_EltMesIssLldpGlobalConfig_ObjectIdentity=ObjectIdentity
eltMesIssLldpGlobalConfig=_EltMesIssLldpGlobalConfig_ObjectIdentity((1,3,6,1,4,1,35265,1,139,10,1,1))
class _EltMesIssLldpduMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('filtering',1),('flooding',2)))
_EltMesIssLldpduMode_Type.__name__=_A
_EltMesIssLldpduMode_Object=MibScalar
eltMesIssLldpduMode=_EltMesIssLldpduMode_Object((1,3,6,1,4,1,35265,1,139,10,1,1,1),_EltMesIssLldpduMode_Type())
eltMesIssLldpduMode.setMaxAccess('read-write')
if mibBuilder.loadTexts:eltMesIssLldpduMode.setStatus('current')
mibBuilder.exportSymbols('ELTEX-MES-ISS-LLDP-MIB',**{'eltMesIssLldpMIB':eltMesIssLldpMIB,'eltMesIssLldpObjects':eltMesIssLldpObjects,'eltMesIssLldpGlobalConfig':eltMesIssLldpGlobalConfig,'eltMesIssLldpduMode':eltMesIssLldpduMode})