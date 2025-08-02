_L='rbnIpBindDisplayGroup'
_K='rbnIpBindContextName'
_J='rbnIpBindCircuitDescr'
_I='rbnIpBindHierarchicalIfIndex'
_H='rbnIpBindIfIndex'
_G='rbnIpBindCircuitHandle'
_F='ifIndex'
_E='IF-MIB'
_D='SnmpAdminString'
_C='read-only'
_B='RBN-IP-BIND-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols(_E,'InterfaceIndexOrZero',_F)
rbnMgmt,=mibBuilder.importSymbols('RBN-SMI','rbnMgmt')
RbnCircuitHandle,=mibBuilder.importSymbols('RBN-TC','RbnCircuitHandle')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rbnIpBindMib=ModuleIdentity((1,3,6,1,4,1,2352,2,26))
if mibBuilder.loadTexts:rbnIpBindMib.setRevisions(('2002-08-20 12:00',))
_RbnIpBindMibNotifications_ObjectIdentity=ObjectIdentity
rbnIpBindMibNotifications=_RbnIpBindMibNotifications_ObjectIdentity((1,3,6,1,4,1,2352,2,26,0))
_RbnIpBindMibObjects_ObjectIdentity=ObjectIdentity
rbnIpBindMibObjects=_RbnIpBindMibObjects_ObjectIdentity((1,3,6,1,4,1,2352,2,26,1))
_RbnIpBindTable_Object=MibTable
rbnIpBindTable=_RbnIpBindTable_Object((1,3,6,1,4,1,2352,2,26,1,1))
if mibBuilder.loadTexts:rbnIpBindTable.setStatus(_A)
_RbnIpBindEntry_Object=MibTableRow
rbnIpBindEntry=_RbnIpBindEntry_Object((1,3,6,1,4,1,2352,2,26,1,1,1))
rbnIpBindEntry.setIndexNames((0,_E,_F),(0,_B,_G))
if mibBuilder.loadTexts:rbnIpBindEntry.setStatus(_A)
_RbnIpBindCircuitHandle_Type=RbnCircuitHandle
_RbnIpBindCircuitHandle_Object=MibTableColumn
rbnIpBindCircuitHandle=_RbnIpBindCircuitHandle_Object((1,3,6,1,4,1,2352,2,26,1,1,1,1),_RbnIpBindCircuitHandle_Type())
rbnIpBindCircuitHandle.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:rbnIpBindCircuitHandle.setStatus(_A)
_RbnIpBindIfIndex_Type=InterfaceIndexOrZero
_RbnIpBindIfIndex_Object=MibTableColumn
rbnIpBindIfIndex=_RbnIpBindIfIndex_Object((1,3,6,1,4,1,2352,2,26,1,1,1,2),_RbnIpBindIfIndex_Type())
rbnIpBindIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIpBindIfIndex.setStatus(_A)
_RbnIpBindHierarchicalIfIndex_Type=InterfaceIndexOrZero
_RbnIpBindHierarchicalIfIndex_Object=MibTableColumn
rbnIpBindHierarchicalIfIndex=_RbnIpBindHierarchicalIfIndex_Object((1,3,6,1,4,1,2352,2,26,1,1,1,3),_RbnIpBindHierarchicalIfIndex_Type())
rbnIpBindHierarchicalIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIpBindHierarchicalIfIndex.setStatus(_A)
class _RbnIpBindCircuitDescr_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,192))
_RbnIpBindCircuitDescr_Type.__name__=_D
_RbnIpBindCircuitDescr_Object=MibTableColumn
rbnIpBindCircuitDescr=_RbnIpBindCircuitDescr_Object((1,3,6,1,4,1,2352,2,26,1,1,1,4),_RbnIpBindCircuitDescr_Type())
rbnIpBindCircuitDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIpBindCircuitDescr.setStatus(_A)
class _RbnIpBindContextName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_RbnIpBindContextName_Type.__name__=_D
_RbnIpBindContextName_Object=MibTableColumn
rbnIpBindContextName=_RbnIpBindContextName_Object((1,3,6,1,4,1,2352,2,26,1,1,1,5),_RbnIpBindContextName_Type())
rbnIpBindContextName.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIpBindContextName.setStatus(_A)
_RbnIpBindMibConformance_ObjectIdentity=ObjectIdentity
rbnIpBindMibConformance=_RbnIpBindMibConformance_ObjectIdentity((1,3,6,1,4,1,2352,2,26,2))
_RbnIpBindCompliances_ObjectIdentity=ObjectIdentity
rbnIpBindCompliances=_RbnIpBindCompliances_ObjectIdentity((1,3,6,1,4,1,2352,2,26,2,1))
_RbnIpBindGroups_ObjectIdentity=ObjectIdentity
rbnIpBindGroups=_RbnIpBindGroups_ObjectIdentity((1,3,6,1,4,1,2352,2,26,2,2))
rbnIpBindDisplayGroup=ObjectGroup((1,3,6,1,4,1,2352,2,26,2,2,1))
rbnIpBindDisplayGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:rbnIpBindDisplayGroup.setStatus(_A)
rbnIpBindCompliance=ModuleCompliance((1,3,6,1,4,1,2352,2,26,2,1,1))
rbnIpBindCompliance.setObjects((_B,_L))
if mibBuilder.loadTexts:rbnIpBindCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'rbnIpBindMib':rbnIpBindMib,'rbnIpBindMibNotifications':rbnIpBindMibNotifications,'rbnIpBindMibObjects':rbnIpBindMibObjects,'rbnIpBindTable':rbnIpBindTable,'rbnIpBindEntry':rbnIpBindEntry,_G:rbnIpBindCircuitHandle,_H:rbnIpBindIfIndex,_I:rbnIpBindHierarchicalIfIndex,_J:rbnIpBindCircuitDescr,_K:rbnIpBindContextName,'rbnIpBindMibConformance':rbnIpBindMibConformance,'rbnIpBindCompliances':rbnIpBindCompliances,'rbnIpBindCompliance':rbnIpBindCompliance,'rbnIpBindGroups':rbnIpBindGroups,_L:rbnIpBindDisplayGroup})