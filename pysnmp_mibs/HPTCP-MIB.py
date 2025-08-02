_D='hpTcpBaseGroup'
_C='hpTcpOutRstsWithAck'
_B='HPTCP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpicfTcpMib=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,79))
if mibBuilder.loadTexts:hpicfTcpMib.setRevisions(('2010-09-30 15:25',))
_HpTcpObjects_ObjectIdentity=ObjectIdentity
hpTcpObjects=_HpTcpObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,79,1))
_HpTcpOutRstsWithAck_Type=Counter32
_HpTcpOutRstsWithAck_Object=MibScalar
hpTcpOutRstsWithAck=_HpTcpOutRstsWithAck_Object((1,3,6,1,4,1,11,2,14,11,5,1,79,1,1),_HpTcpOutRstsWithAck_Type())
hpTcpOutRstsWithAck.setMaxAccess('read-only')
if mibBuilder.loadTexts:hpTcpOutRstsWithAck.setStatus(_A)
_HpTcpConformance_ObjectIdentity=ObjectIdentity
hpTcpConformance=_HpTcpConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,79,2))
_HpTcpGroups_ObjectIdentity=ObjectIdentity
hpTcpGroups=_HpTcpGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,79,2,1))
_HpTcpCompliances_ObjectIdentity=ObjectIdentity
hpTcpCompliances=_HpTcpCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,79,2,2))
hpTcpBaseGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,79,2,1,1))
hpTcpBaseGroup.setObjects((_B,_C))
if mibBuilder.loadTexts:hpTcpBaseGroup.setStatus(_A)
hpTcpCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,79,2,2,1))
hpTcpCompliance.setObjects((_B,_D))
if mibBuilder.loadTexts:hpTcpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpicfTcpMib':hpicfTcpMib,'hpTcpObjects':hpTcpObjects,_C:hpTcpOutRstsWithAck,'hpTcpConformance':hpTcpConformance,'hpTcpGroups':hpTcpGroups,_D:hpTcpBaseGroup,'hpTcpCompliances':hpTcpCompliances,'hpTcpCompliance':hpTcpCompliance})