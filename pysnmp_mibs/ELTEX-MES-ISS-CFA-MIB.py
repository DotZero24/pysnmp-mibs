_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltMesIss,=mibBuilder.importSymbols('ELTEX-MES-ISS-MIB','eltMesIss')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
eltMesIssCfaMIB=ModuleIdentity((1,3,6,1,4,1,35265,1,139,20))
if mibBuilder.loadTexts:eltMesIssCfaMIB.setRevisions(('2020-05-25 00:00',))
_EltMesIssCfaObjects_ObjectIdentity=ObjectIdentity
eltMesIssCfaObjects=_EltMesIssCfaObjects_ObjectIdentity((1,3,6,1,4,1,35265,1,139,20,1))
_EltMesIssCfaGlobals_ObjectIdentity=ObjectIdentity
eltMesIssCfaGlobals=_EltMesIssCfaGlobals_ObjectIdentity((1,3,6,1,4,1,35265,1,139,20,1,1))
class _EltMesIssCfaGlobalMtu_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(128,12288))
_EltMesIssCfaGlobalMtu_Type.__name__=_A
_EltMesIssCfaGlobalMtu_Object=MibScalar
eltMesIssCfaGlobalMtu=_EltMesIssCfaGlobalMtu_Object((1,3,6,1,4,1,35265,1,139,20,1,1,1),_EltMesIssCfaGlobalMtu_Type())
eltMesIssCfaGlobalMtu.setMaxAccess('read-write')
if mibBuilder.loadTexts:eltMesIssCfaGlobalMtu.setStatus('current')
_EltMesIssCfaNotifications_ObjectIdentity=ObjectIdentity
eltMesIssCfaNotifications=_EltMesIssCfaNotifications_ObjectIdentity((1,3,6,1,4,1,35265,1,139,20,2))
mibBuilder.exportSymbols('ELTEX-MES-ISS-CFA-MIB',**{'eltMesIssCfaMIB':eltMesIssCfaMIB,'eltMesIssCfaObjects':eltMesIssCfaObjects,'eltMesIssCfaGlobals':eltMesIssCfaGlobals,'eltMesIssCfaGlobalMtu':eltMesIssCfaGlobalMtu,'eltMesIssCfaNotifications':eltMesIssCfaNotifications})