_B='current'
_A='read-write'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelRouter=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,113))
_ZyxelRouterNsf_ObjectIdentity=ObjectIdentity
zyxelRouterNsf=_ZyxelRouterNsf_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,113,1))
_ZyxelRouterNsfSetup_ObjectIdentity=ObjectIdentity
zyxelRouterNsfSetup=_ZyxelRouterNsfSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,113,1,1))
_ZyRouterNsfEnable_Type=EnabledStatus
_ZyRouterNsfEnable_Object=MibScalar
zyRouterNsfEnable=_ZyRouterNsfEnable_Object((1,3,6,1,4,1,890,1,15,3,113,1,1,1),_ZyRouterNsfEnable_Type())
zyRouterNsfEnable.setMaxAccess(_A)
if mibBuilder.loadTexts:zyRouterNsfEnable.setStatus(_B)
_ZyRouterNsfTimer_Type=Integer32
_ZyRouterNsfTimer_Object=MibScalar
zyRouterNsfTimer=_ZyRouterNsfTimer_Object((1,3,6,1,4,1,890,1,15,3,113,1,1,2),_ZyRouterNsfTimer_Type())
zyRouterNsfTimer.setMaxAccess(_A)
if mibBuilder.loadTexts:zyRouterNsfTimer.setStatus(_B)
mibBuilder.exportSymbols('ZYXEL-ROUTER-MIB',**{'zyxelRouter':zyxelRouter,'zyxelRouterNsf':zyxelRouterNsf,'zyxelRouterNsfSetup':zyxelRouterNsfSetup,'zyRouterNsfEnable':zyRouterNsfEnable,'zyRouterNsfTimer':zyRouterNsfTimer})