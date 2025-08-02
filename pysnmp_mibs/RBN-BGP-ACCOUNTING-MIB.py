_P='rbnBpaTableGroup1'
_O='rbnBpaTableGroup'
_N='rbnBpaContextName'
_M='rbnBpaInterfaceName'
_L='rbnBpaCircuitDescr'
_K='deprecated'
_J='Integer32'
_I='ifIndex'
_H='IF-MIB'
_G='rbnBpaInOctetCount'
_F='rbnBpaInPacketCount'
_E='rbnBpaBucketIndex'
_D='SnmpAdminString'
_C='read-only'
_B='current'
_A='RBN-BGP-ACCOUNTING-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_H,_I)
rbnMgmt,=mibBuilder.importSymbols('RBN-SMI','rbnMgmt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rbnBgpPolAcctMIB=ModuleIdentity((1,3,6,1,4,1,2352,2,20))
if mibBuilder.loadTexts:rbnBgpPolAcctMIB.setRevisions(('2005-09-20 00:00','2002-03-15 00:00'))
_RbnBgpPolAcctMIBObjects_ObjectIdentity=ObjectIdentity
rbnBgpPolAcctMIBObjects=_RbnBgpPolAcctMIBObjects_ObjectIdentity((1,3,6,1,4,1,2352,2,20,1))
_RbnBpaTable_Object=MibTable
rbnBpaTable=_RbnBpaTable_Object((1,3,6,1,4,1,2352,2,20,1,1))
if mibBuilder.loadTexts:rbnBpaTable.setStatus(_B)
_RbnBpaEntry_Object=MibTableRow
rbnBpaEntry=_RbnBpaEntry_Object((1,3,6,1,4,1,2352,2,20,1,1,1))
rbnBpaEntry.setIndexNames((0,_H,_I),(0,_A,_E))
if mibBuilder.loadTexts:rbnBpaEntry.setStatus(_B)
class _RbnBpaBucketIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RbnBpaBucketIndex_Type.__name__=_J
_RbnBpaBucketIndex_Object=MibTableColumn
rbnBpaBucketIndex=_RbnBpaBucketIndex_Object((1,3,6,1,4,1,2352,2,20,1,1,1,1),_RbnBpaBucketIndex_Type())
rbnBpaBucketIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnBpaBucketIndex.setStatus(_B)
_RbnBpaInPacketCount_Type=Counter64
_RbnBpaInPacketCount_Object=MibTableColumn
rbnBpaInPacketCount=_RbnBpaInPacketCount_Object((1,3,6,1,4,1,2352,2,20,1,1,1,2),_RbnBpaInPacketCount_Type())
rbnBpaInPacketCount.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnBpaInPacketCount.setStatus(_B)
_RbnBpaInOctetCount_Type=Counter64
_RbnBpaInOctetCount_Object=MibTableColumn
rbnBpaInOctetCount=_RbnBpaInOctetCount_Object((1,3,6,1,4,1,2352,2,20,1,1,1,3),_RbnBpaInOctetCount_Type())
rbnBpaInOctetCount.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnBpaInOctetCount.setStatus(_B)
class _RbnBpaCircuitDescr_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,192))
_RbnBpaCircuitDescr_Type.__name__=_D
_RbnBpaCircuitDescr_Object=MibTableColumn
rbnBpaCircuitDescr=_RbnBpaCircuitDescr_Object((1,3,6,1,4,1,2352,2,20,1,1,1,4),_RbnBpaCircuitDescr_Type())
rbnBpaCircuitDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnBpaCircuitDescr.setStatus(_B)
class _RbnBpaInterfaceName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_RbnBpaInterfaceName_Type.__name__=_D
_RbnBpaInterfaceName_Object=MibTableColumn
rbnBpaInterfaceName=_RbnBpaInterfaceName_Object((1,3,6,1,4,1,2352,2,20,1,1,1,5),_RbnBpaInterfaceName_Type())
rbnBpaInterfaceName.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnBpaInterfaceName.setStatus(_B)
class _RbnBpaContextName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_RbnBpaContextName_Type.__name__=_D
_RbnBpaContextName_Object=MibTableColumn
rbnBpaContextName=_RbnBpaContextName_Object((1,3,6,1,4,1,2352,2,20,1,1,1,6),_RbnBpaContextName_Type())
rbnBpaContextName.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnBpaContextName.setStatus(_B)
_RbnBgpPolAcctMIBConformance_ObjectIdentity=ObjectIdentity
rbnBgpPolAcctMIBConformance=_RbnBgpPolAcctMIBConformance_ObjectIdentity((1,3,6,1,4,1,2352,2,20,3))
_RbnBgpPolAcctMIBCompliances_ObjectIdentity=ObjectIdentity
rbnBgpPolAcctMIBCompliances=_RbnBgpPolAcctMIBCompliances_ObjectIdentity((1,3,6,1,4,1,2352,2,20,3,1))
_RbnBgpPolAcctMIBGroups_ObjectIdentity=ObjectIdentity
rbnBgpPolAcctMIBGroups=_RbnBgpPolAcctMIBGroups_ObjectIdentity((1,3,6,1,4,1,2352,2,20,3,2))
rbnBpaTableGroup=ObjectGroup((1,3,6,1,4,1,2352,2,20,3,2,1))
rbnBpaTableGroup.setObjects(*((_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:rbnBpaTableGroup.setStatus(_K)
rbnBpaTableGroup1=ObjectGroup((1,3,6,1,4,1,2352,2,20,3,2,2))
rbnBpaTableGroup1.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:rbnBpaTableGroup1.setStatus(_B)
rbnBgpPolAcctMIBCompliance=ModuleCompliance((1,3,6,1,4,1,2352,2,20,3,1,1))
rbnBgpPolAcctMIBCompliance.setObjects((_A,_O))
if mibBuilder.loadTexts:rbnBgpPolAcctMIBCompliance.setStatus(_K)
rbnBgpPolAcctMIBCompliance1=ModuleCompliance((1,3,6,1,4,1,2352,2,20,3,1,2))
rbnBgpPolAcctMIBCompliance1.setObjects((_A,_P))
if mibBuilder.loadTexts:rbnBgpPolAcctMIBCompliance1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'rbnBgpPolAcctMIB':rbnBgpPolAcctMIB,'rbnBgpPolAcctMIBObjects':rbnBgpPolAcctMIBObjects,'rbnBpaTable':rbnBpaTable,'rbnBpaEntry':rbnBpaEntry,_E:rbnBpaBucketIndex,_F:rbnBpaInPacketCount,_G:rbnBpaInOctetCount,_L:rbnBpaCircuitDescr,_M:rbnBpaInterfaceName,_N:rbnBpaContextName,'rbnBgpPolAcctMIBConformance':rbnBgpPolAcctMIBConformance,'rbnBgpPolAcctMIBCompliances':rbnBgpPolAcctMIBCompliances,'rbnBgpPolAcctMIBCompliance':rbnBgpPolAcctMIBCompliance,'rbnBgpPolAcctMIBCompliance1':rbnBgpPolAcctMIBCompliance1,'rbnBgpPolAcctMIBGroups':rbnBgpPolAcctMIBGroups,_O:rbnBpaTableGroup,_P:rbnBpaTableGroup1})