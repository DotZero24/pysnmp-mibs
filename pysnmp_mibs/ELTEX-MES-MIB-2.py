_A='DisplayString'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltMesMng,=mibBuilder.importSymbols('ELTEX-MES','eltMesMng')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_A,'PhysAddress','TextualConvention')
elt_mes_mib_2=ModuleIdentity((1,3,6,1,4,1,35265,1,23,1,1))
_EltMesIfMIB_ObjectIdentity=ObjectIdentity
eltMesIfMIB=_EltMesIfMIB_ObjectIdentity((1,3,6,1,4,1,35265,1,23,1,1,31))
_EltMesSystem_ObjectIdentity=ObjectIdentity
eltMesSystem=_EltMesSystem_ObjectIdentity((1,3,6,1,4,1,35265,1,23,1,1,32))
class _EltSysDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_EltSysDescr_Type.__name__=_A
_EltSysDescr_Object=MibScalar
eltSysDescr=_EltSysDescr_Object((1,3,6,1,4,1,35265,1,23,1,1,32,1),_EltSysDescr_Type())
eltSysDescr.setMaxAccess('read-write')
if mibBuilder.loadTexts:eltSysDescr.setStatus('current')
mibBuilder.exportSymbols('ELTEX-MES-MIB-2',**{'elt-mes-mib-2':elt_mes_mib_2,'eltMesIfMIB':eltMesIfMIB,'eltMesSystem':eltMesSystem,'eltSysDescr':eltSysDescr})