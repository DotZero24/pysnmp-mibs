_F='read-write'
_E='zyRouteDomainIpMaskBits'
_D='zyRouteDomainIpAddress'
_C='Integer32'
_B='ZYXEL-IP-FORWARD-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyRouteDomainIpAddress,zyRouteDomainIpMaskBits=mibBuilder.importSymbols(_B,_D,_E)
zyxelIgmp=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,29))
_ZyxelIgmpSetup_ObjectIdentity=ObjectIdentity
zyxelIgmpSetup=_ZyxelIgmpSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,29,1))
_ZyIgmpState_Type=EnabledStatus
_ZyIgmpState_Object=MibScalar
zyIgmpState=_ZyIgmpState_Object((1,3,6,1,4,1,890,1,15,3,29,1,1),_ZyIgmpState_Type())
zyIgmpState.setMaxAccess(_F)
if mibBuilder.loadTexts:zyIgmpState.setStatus(_A)
_ZyxelIgmpRouteDomainTable_Object=MibTable
zyxelIgmpRouteDomainTable=_ZyxelIgmpRouteDomainTable_Object((1,3,6,1,4,1,890,1,15,3,29,1,2))
if mibBuilder.loadTexts:zyxelIgmpRouteDomainTable.setStatus(_A)
_ZyxelIgmpRouteDomainEntry_Object=MibTableRow
zyxelIgmpRouteDomainEntry=_ZyxelIgmpRouteDomainEntry_Object((1,3,6,1,4,1,890,1,15,3,29,1,2,1))
zyxelIgmpRouteDomainEntry.setIndexNames((0,_B,_D),(0,_B,_E))
if mibBuilder.loadTexts:zyxelIgmpRouteDomainEntry.setStatus(_A)
class _ZyIgmpRouteDomainVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('igmpV1',1),('igmpV2',2),('igmpV3',3)))
_ZyIgmpRouteDomainVersion_Type.__name__=_C
_ZyIgmpRouteDomainVersion_Object=MibTableColumn
zyIgmpRouteDomainVersion=_ZyIgmpRouteDomainVersion_Object((1,3,6,1,4,1,890,1,15,3,29,1,2,1,1),_ZyIgmpRouteDomainVersion_Type())
zyIgmpRouteDomainVersion.setMaxAccess(_F)
if mibBuilder.loadTexts:zyIgmpRouteDomainVersion.setStatus(_A)
mibBuilder.exportSymbols('ZYXEL-IGMP-MIB',**{'zyxelIgmp':zyxelIgmp,'zyxelIgmpSetup':zyxelIgmpSetup,'zyIgmpState':zyIgmpState,'zyxelIgmpRouteDomainTable':zyxelIgmpRouteDomainTable,'zyxelIgmpRouteDomainEntry':zyxelIgmpRouteDomainEntry,'zyIgmpRouteDomainVersion':zyIgmpRouteDomainVersion})