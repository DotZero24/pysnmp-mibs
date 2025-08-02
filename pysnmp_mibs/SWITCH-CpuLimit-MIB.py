if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
iscomSwitch,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','iscomSwitch')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
EnableVar,=mibBuilder.importSymbols('SWITCH-TC','EnableVar')
rcCpuLimit=ModuleIdentity((1,3,6,1,4,1,8886,6,1,61))
if mibBuilder.loadTexts:rcCpuLimit.setRevisions(('2010-04-01 00:00',))
_RcCpuLimitGroup_ObjectIdentity=ObjectIdentity
rcCpuLimitGroup=_RcCpuLimitGroup_ObjectIdentity((1,3,6,1,4,1,8886,6,1,61,1))
_RcCpuLimitEnable_Type=EnableVar
_RcCpuLimitEnable_Object=MibScalar
rcCpuLimitEnable=_RcCpuLimitEnable_Object((1,3,6,1,4,1,8886,6,1,61,1,1),_RcCpuLimitEnable_Type())
rcCpuLimitEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:rcCpuLimitEnable.setStatus('current')
mibBuilder.exportSymbols('SWITCH-CpuLimit-MIB',**{'rcCpuLimit':rcCpuLimit,'rcCpuLimitGroup':rcCpuLimitGroup,'rcCpuLimitEnable':rcCpuLimitEnable})