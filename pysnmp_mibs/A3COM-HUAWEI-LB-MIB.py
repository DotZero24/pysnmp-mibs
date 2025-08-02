_H='h3cLBRealServerConnectNumber'
_G='accessible-for-notify'
_F='Integer32'
_E='h3cLBRealServerName'
_D='DisplayString'
_C='h3cLBRealServerGroupName'
_B='A3COM-HUAWEI-LB-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','h3cCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
h3cLB=ModuleIdentity((1,3,6,1,4,1,43,45,1,10,2,116))
if mibBuilder.loadTexts:h3cLB.setRevisions(('2010-12-01 00:00',))
_H3cLBTables_ObjectIdentity=ObjectIdentity
h3cLBTables=_H3cLBTables_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,116,1))
_H3cLBRealServerGroupTable_Object=MibTable
h3cLBRealServerGroupTable=_H3cLBRealServerGroupTable_Object((1,3,6,1,4,1,43,45,1,10,2,116,1,1))
if mibBuilder.loadTexts:h3cLBRealServerGroupTable.setStatus(_A)
_H3cLBRealServerGroupEntry_Object=MibTableRow
h3cLBRealServerGroupEntry=_H3cLBRealServerGroupEntry_Object((1,3,6,1,4,1,43,45,1,10,2,116,1,1,1))
h3cLBRealServerGroupEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:h3cLBRealServerGroupEntry.setStatus(_A)
class _H3cLBRealServerGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_H3cLBRealServerGroupName_Type.__name__=_D
_H3cLBRealServerGroupName_Object=MibTableColumn
h3cLBRealServerGroupName=_H3cLBRealServerGroupName_Object((1,3,6,1,4,1,43,45,1,10,2,116,1,1,1,1),_H3cLBRealServerGroupName_Type())
h3cLBRealServerGroupName.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cLBRealServerGroupName.setStatus(_A)
_H3cLBRealServerTable_Object=MibTable
h3cLBRealServerTable=_H3cLBRealServerTable_Object((1,3,6,1,4,1,43,45,1,10,2,116,1,2))
if mibBuilder.loadTexts:h3cLBRealServerTable.setStatus(_A)
_H3cLBRealServerEntry_Object=MibTableRow
h3cLBRealServerEntry=_H3cLBRealServerEntry_Object((1,3,6,1,4,1,43,45,1,10,2,116,1,2,1))
h3cLBRealServerEntry.setIndexNames((0,_B,_C),(0,_B,_E))
if mibBuilder.loadTexts:h3cLBRealServerEntry.setStatus(_A)
class _H3cLBRealServerName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_H3cLBRealServerName_Type.__name__=_D
_H3cLBRealServerName_Object=MibTableColumn
h3cLBRealServerName=_H3cLBRealServerName_Object((1,3,6,1,4,1,43,45,1,10,2,116,1,2,1,1),_H3cLBRealServerName_Type())
h3cLBRealServerName.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cLBRealServerName.setStatus(_A)
class _H3cLBRealServerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('enabled',1),('disabled',2),('slowdown',3)))
_H3cLBRealServerStatus_Type.__name__=_F
_H3cLBRealServerStatus_Object=MibTableColumn
h3cLBRealServerStatus=_H3cLBRealServerStatus_Object((1,3,6,1,4,1,43,45,1,10,2,116,1,2,1,2),_H3cLBRealServerStatus_Type())
h3cLBRealServerStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:h3cLBRealServerStatus.setStatus(_A)
_H3cLBRealServerConnectNumber_Type=Integer32
_H3cLBRealServerConnectNumber_Object=MibTableColumn
h3cLBRealServerConnectNumber=_H3cLBRealServerConnectNumber_Object((1,3,6,1,4,1,43,45,1,10,2,116,1,2,1,3),_H3cLBRealServerConnectNumber_Type())
h3cLBRealServerConnectNumber.setMaxAccess('read-only')
if mibBuilder.loadTexts:h3cLBRealServerConnectNumber.setStatus(_A)
_H3cLBTrap_ObjectIdentity=ObjectIdentity
h3cLBTrap=_H3cLBTrap_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,116,2))
_H3cLBTrapPrex_ObjectIdentity=ObjectIdentity
h3cLBTrapPrex=_H3cLBTrapPrex_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,116,2,0))
h3cLBRealServerOverLoad=NotificationType((1,3,6,1,4,1,43,45,1,10,2,116,2,0,1))
h3cLBRealServerOverLoad.setObjects(*((_B,_C),(_B,_E),(_B,_H)))
if mibBuilder.loadTexts:h3cLBRealServerOverLoad.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'h3cLB':h3cLB,'h3cLBTables':h3cLBTables,'h3cLBRealServerGroupTable':h3cLBRealServerGroupTable,'h3cLBRealServerGroupEntry':h3cLBRealServerGroupEntry,_C:h3cLBRealServerGroupName,'h3cLBRealServerTable':h3cLBRealServerTable,'h3cLBRealServerEntry':h3cLBRealServerEntry,_E:h3cLBRealServerName,'h3cLBRealServerStatus':h3cLBRealServerStatus,_H:h3cLBRealServerConnectNumber,'h3cLBTrap':h3cLBTrap,'h3cLBTrapPrex':h3cLBTrapPrex,'h3cLBRealServerOverLoad':h3cLBRealServerOverLoad})