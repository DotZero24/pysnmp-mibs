_K='ntwsApUnconfOrphanBasicGroup'
_J='ntwsApUnconfOrphanReason'
_I='ntwsApUnconfOrphanVLANName'
_H='ntwsApUnconfOrphanPhysPortNum'
_G='ntwsApUnconfOrphanIpAddress'
_F='ntwsApUnconfOrphanApModelName'
_E='ntwsApUnconfOrphanApSerialNum'
_D='DisplayString'
_C='read-only'
_B='NTWS-AP-UNCONFIGURED-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
NtwsApSerialNum,=mibBuilder.importSymbols('NTWS-AP-TC','NtwsApSerialNum')
NtwsPhysPortNumber,=mibBuilder.importSymbols('NTWS-BASIC-TC','NtwsPhysPortNumber')
ntwsMibs,=mibBuilder.importSymbols('NTWS-ROOT-MIB','ntwsMibs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
ntwsApUnconfiguredMib=ModuleIdentity((1,3,6,1,4,1,45,6,1,4,15))
if mibBuilder.loadTexts:ntwsApUnconfiguredMib.setRevisions(('2008-11-14 00:04',))
class NtwsApUnconfiguredOrphanReason(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('other',1),('no-configuration',2),('ap-license-exceeded',3),('controller-behind-nat',4),('ap-model-mismatch',5),('no-macs',6)))
_NtwsApUnconfMibObjects_ObjectIdentity=ObjectIdentity
ntwsApUnconfMibObjects=_NtwsApUnconfMibObjects_ObjectIdentity((1,3,6,1,4,1,45,6,1,4,15,1))
_NtwsApUnconfOrphanTable_Object=MibTable
ntwsApUnconfOrphanTable=_NtwsApUnconfOrphanTable_Object((1,3,6,1,4,1,45,6,1,4,15,1,2))
if mibBuilder.loadTexts:ntwsApUnconfOrphanTable.setStatus(_A)
_NtwsApUnconfOrphanEntry_Object=MibTableRow
ntwsApUnconfOrphanEntry=_NtwsApUnconfOrphanEntry_Object((1,3,6,1,4,1,45,6,1,4,15,1,2,1))
ntwsApUnconfOrphanEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:ntwsApUnconfOrphanEntry.setStatus(_A)
_NtwsApUnconfOrphanApSerialNum_Type=NtwsApSerialNum
_NtwsApUnconfOrphanApSerialNum_Object=MibTableColumn
ntwsApUnconfOrphanApSerialNum=_NtwsApUnconfOrphanApSerialNum_Object((1,3,6,1,4,1,45,6,1,4,15,1,2,1,1),_NtwsApUnconfOrphanApSerialNum_Type())
ntwsApUnconfOrphanApSerialNum.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ntwsApUnconfOrphanApSerialNum.setStatus(_A)
class _NtwsApUnconfOrphanApModelName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_NtwsApUnconfOrphanApModelName_Type.__name__=_D
_NtwsApUnconfOrphanApModelName_Object=MibTableColumn
ntwsApUnconfOrphanApModelName=_NtwsApUnconfOrphanApModelName_Object((1,3,6,1,4,1,45,6,1,4,15,1,2,1,2),_NtwsApUnconfOrphanApModelName_Type())
ntwsApUnconfOrphanApModelName.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsApUnconfOrphanApModelName.setStatus(_A)
_NtwsApUnconfOrphanIpAddress_Type=IpAddress
_NtwsApUnconfOrphanIpAddress_Object=MibTableColumn
ntwsApUnconfOrphanIpAddress=_NtwsApUnconfOrphanIpAddress_Object((1,3,6,1,4,1,45,6,1,4,15,1,2,1,5),_NtwsApUnconfOrphanIpAddress_Type())
ntwsApUnconfOrphanIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsApUnconfOrphanIpAddress.setStatus(_A)
_NtwsApUnconfOrphanPhysPortNum_Type=NtwsPhysPortNumber
_NtwsApUnconfOrphanPhysPortNum_Object=MibTableColumn
ntwsApUnconfOrphanPhysPortNum=_NtwsApUnconfOrphanPhysPortNum_Object((1,3,6,1,4,1,45,6,1,4,15,1,2,1,6),_NtwsApUnconfOrphanPhysPortNum_Type())
ntwsApUnconfOrphanPhysPortNum.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsApUnconfOrphanPhysPortNum.setStatus(_A)
class _NtwsApUnconfOrphanVLANName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NtwsApUnconfOrphanVLANName_Type.__name__=_D
_NtwsApUnconfOrphanVLANName_Object=MibTableColumn
ntwsApUnconfOrphanVLANName=_NtwsApUnconfOrphanVLANName_Object((1,3,6,1,4,1,45,6,1,4,15,1,2,1,7),_NtwsApUnconfOrphanVLANName_Type())
ntwsApUnconfOrphanVLANName.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsApUnconfOrphanVLANName.setStatus(_A)
_NtwsApUnconfOrphanReason_Type=NtwsApUnconfiguredOrphanReason
_NtwsApUnconfOrphanReason_Object=MibTableColumn
ntwsApUnconfOrphanReason=_NtwsApUnconfOrphanReason_Object((1,3,6,1,4,1,45,6,1,4,15,1,2,1,8),_NtwsApUnconfOrphanReason_Type())
ntwsApUnconfOrphanReason.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsApUnconfOrphanReason.setStatus(_A)
_NtwsApUnconfConformance_ObjectIdentity=ObjectIdentity
ntwsApUnconfConformance=_NtwsApUnconfConformance_ObjectIdentity((1,3,6,1,4,1,45,6,1,4,15,2))
_NtwsApUnconfCompliances_ObjectIdentity=ObjectIdentity
ntwsApUnconfCompliances=_NtwsApUnconfCompliances_ObjectIdentity((1,3,6,1,4,1,45,6,1,4,15,2,1))
_NtwsApUnconfGroups_ObjectIdentity=ObjectIdentity
ntwsApUnconfGroups=_NtwsApUnconfGroups_ObjectIdentity((1,3,6,1,4,1,45,6,1,4,15,2,2))
ntwsApUnconfOrphanBasicGroup=ObjectGroup((1,3,6,1,4,1,45,6,1,4,15,2,2,1))
ntwsApUnconfOrphanBasicGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:ntwsApUnconfOrphanBasicGroup.setStatus(_A)
ntwsApUnconfCompliance=ModuleCompliance((1,3,6,1,4,1,45,6,1,4,15,2,1,1))
ntwsApUnconfCompliance.setObjects((_B,_K))
if mibBuilder.loadTexts:ntwsApUnconfCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'NtwsApUnconfiguredOrphanReason':NtwsApUnconfiguredOrphanReason,'ntwsApUnconfiguredMib':ntwsApUnconfiguredMib,'ntwsApUnconfMibObjects':ntwsApUnconfMibObjects,'ntwsApUnconfOrphanTable':ntwsApUnconfOrphanTable,'ntwsApUnconfOrphanEntry':ntwsApUnconfOrphanEntry,_E:ntwsApUnconfOrphanApSerialNum,_F:ntwsApUnconfOrphanApModelName,_G:ntwsApUnconfOrphanIpAddress,_H:ntwsApUnconfOrphanPhysPortNum,_I:ntwsApUnconfOrphanVLANName,_J:ntwsApUnconfOrphanReason,'ntwsApUnconfConformance':ntwsApUnconfConformance,'ntwsApUnconfCompliances':ntwsApUnconfCompliances,'ntwsApUnconfCompliance':ntwsApUnconfCompliance,'ntwsApUnconfGroups':ntwsApUnconfGroups,_K:ntwsApUnconfOrphanBasicGroup})