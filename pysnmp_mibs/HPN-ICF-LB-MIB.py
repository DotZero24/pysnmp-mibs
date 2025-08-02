_H='hpnicfLBRealServerConnectNumber'
_G='accessible-for-notify'
_F='Integer32'
_E='hpnicfLBRealServerName'
_D='DisplayString'
_C='hpnicfLBRealServerGroupName'
_B='HPN-ICF-LB-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
hpnicfLB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,116))
if mibBuilder.loadTexts:hpnicfLB.setRevisions(('2010-12-01 00:00',))
_HpnicfLBTables_ObjectIdentity=ObjectIdentity
hpnicfLBTables=_HpnicfLBTables_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,116,1))
_HpnicfLBRealServerGroupTable_Object=MibTable
hpnicfLBRealServerGroupTable=_HpnicfLBRealServerGroupTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,116,1,1))
if mibBuilder.loadTexts:hpnicfLBRealServerGroupTable.setStatus(_A)
_HpnicfLBRealServerGroupEntry_Object=MibTableRow
hpnicfLBRealServerGroupEntry=_HpnicfLBRealServerGroupEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,116,1,1,1))
hpnicfLBRealServerGroupEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:hpnicfLBRealServerGroupEntry.setStatus(_A)
class _HpnicfLBRealServerGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_HpnicfLBRealServerGroupName_Type.__name__=_D
_HpnicfLBRealServerGroupName_Object=MibTableColumn
hpnicfLBRealServerGroupName=_HpnicfLBRealServerGroupName_Object((1,3,6,1,4,1,11,2,14,11,15,2,116,1,1,1,1),_HpnicfLBRealServerGroupName_Type())
hpnicfLBRealServerGroupName.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfLBRealServerGroupName.setStatus(_A)
_HpnicfLBRealServerTable_Object=MibTable
hpnicfLBRealServerTable=_HpnicfLBRealServerTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,116,1,2))
if mibBuilder.loadTexts:hpnicfLBRealServerTable.setStatus(_A)
_HpnicfLBRealServerEntry_Object=MibTableRow
hpnicfLBRealServerEntry=_HpnicfLBRealServerEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,116,1,2,1))
hpnicfLBRealServerEntry.setIndexNames((0,_B,_C),(0,_B,_E))
if mibBuilder.loadTexts:hpnicfLBRealServerEntry.setStatus(_A)
class _HpnicfLBRealServerName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_HpnicfLBRealServerName_Type.__name__=_D
_HpnicfLBRealServerName_Object=MibTableColumn
hpnicfLBRealServerName=_HpnicfLBRealServerName_Object((1,3,6,1,4,1,11,2,14,11,15,2,116,1,2,1,1),_HpnicfLBRealServerName_Type())
hpnicfLBRealServerName.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfLBRealServerName.setStatus(_A)
class _HpnicfLBRealServerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('enabled',1),('disabled',2),('slowdown',3)))
_HpnicfLBRealServerStatus_Type.__name__=_F
_HpnicfLBRealServerStatus_Object=MibTableColumn
hpnicfLBRealServerStatus=_HpnicfLBRealServerStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,116,1,2,1,2),_HpnicfLBRealServerStatus_Type())
hpnicfLBRealServerStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:hpnicfLBRealServerStatus.setStatus(_A)
_HpnicfLBRealServerConnectNumber_Type=Integer32
_HpnicfLBRealServerConnectNumber_Object=MibTableColumn
hpnicfLBRealServerConnectNumber=_HpnicfLBRealServerConnectNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,116,1,2,1,3),_HpnicfLBRealServerConnectNumber_Type())
hpnicfLBRealServerConnectNumber.setMaxAccess('read-only')
if mibBuilder.loadTexts:hpnicfLBRealServerConnectNumber.setStatus(_A)
_HpnicfLBTrap_ObjectIdentity=ObjectIdentity
hpnicfLBTrap=_HpnicfLBTrap_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,116,2))
_HpnicfLBTrapPrex_ObjectIdentity=ObjectIdentity
hpnicfLBTrapPrex=_HpnicfLBTrapPrex_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,116,2,0))
hpnicfLBRealServerOverLoad=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,116,2,0,1))
hpnicfLBRealServerOverLoad.setObjects(*((_B,_C),(_B,_E),(_B,_H)))
if mibBuilder.loadTexts:hpnicfLBRealServerOverLoad.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpnicfLB':hpnicfLB,'hpnicfLBTables':hpnicfLBTables,'hpnicfLBRealServerGroupTable':hpnicfLBRealServerGroupTable,'hpnicfLBRealServerGroupEntry':hpnicfLBRealServerGroupEntry,_C:hpnicfLBRealServerGroupName,'hpnicfLBRealServerTable':hpnicfLBRealServerTable,'hpnicfLBRealServerEntry':hpnicfLBRealServerEntry,_E:hpnicfLBRealServerName,'hpnicfLBRealServerStatus':hpnicfLBRealServerStatus,_H:hpnicfLBRealServerConnectNumber,'hpnicfLBTrap':hpnicfLBTrap,'hpnicfLBTrapPrex':hpnicfLBTrapPrex,'hpnicfLBRealServerOverLoad':hpnicfLBRealServerOverLoad})