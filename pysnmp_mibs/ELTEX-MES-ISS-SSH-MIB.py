if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltMesIss,=mibBuilder.importSymbols('ELTEX-MES-ISS-MIB','eltMesIss')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
eltMesIssSshMIB=ModuleIdentity((1,3,6,1,4,1,35265,1,139,30))
if mibBuilder.loadTexts:eltMesIssSshMIB.setRevisions(('2022-04-19 00:00',))
_EltMesIssSshObjects_ObjectIdentity=ObjectIdentity
eltMesIssSshObjects=_EltMesIssSshObjects_ObjectIdentity((1,3,6,1,4,1,35265,1,139,30,1))
_EltMesIssSshGlobals_ObjectIdentity=ObjectIdentity
eltMesIssSshGlobals=_EltMesIssSshGlobals_ObjectIdentity((1,3,6,1,4,1,35265,1,139,30,1,1))
class _EltMesIssSshAuthTypes_Type(Bits):defaultHexValue='80';namedValues=NamedValues(*(('password',0),('publickey',1)))
_EltMesIssSshAuthTypes_Type.__name__='Bits'
_EltMesIssSshAuthTypes_Object=MibScalar
eltMesIssSshAuthTypes=_EltMesIssSshAuthTypes_Object((1,3,6,1,4,1,35265,1,139,30,1,1,1),_EltMesIssSshAuthTypes_Type())
eltMesIssSshAuthTypes.setMaxAccess('read-write')
if mibBuilder.loadTexts:eltMesIssSshAuthTypes.setStatus('current')
mibBuilder.exportSymbols('ELTEX-MES-ISS-SSH-MIB',**{'eltMesIssSshMIB':eltMesIssSshMIB,'eltMesIssSshObjects':eltMesIssSshObjects,'eltMesIssSshGlobals':eltMesIssSshGlobals,'eltMesIssSshAuthTypes':eltMesIssSshAuthTypes})