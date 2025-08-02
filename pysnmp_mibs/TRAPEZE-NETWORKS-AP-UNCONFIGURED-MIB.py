_K='trpzApUnconfOrphanBasicGroup'
_J='trpzApUnconfOrphanReason'
_I='trpzApUnconfOrphanVLANName'
_H='trpzApUnconfOrphanPhysPortNum'
_G='trpzApUnconfOrphanIpAddress'
_F='trpzApUnconfOrphanApModelName'
_E='trpzApUnconfOrphanApSerialNum'
_D='DisplayString'
_C='read-only'
_B='TRAPEZE-NETWORKS-AP-UNCONFIGURED-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
TrpzApSerialNum,=mibBuilder.importSymbols('TRAPEZE-NETWORKS-AP-TC','TrpzApSerialNum')
TrpzPhysPortNumber,=mibBuilder.importSymbols('TRAPEZE-NETWORKS-BASIC-TC','TrpzPhysPortNumber')
trpzMibs,=mibBuilder.importSymbols('TRAPEZE-NETWORKS-ROOT-MIB','trpzMibs')
trpzApUnconfiguredMib=ModuleIdentity((1,3,6,1,4,1,14525,4,15))
if mibBuilder.loadTexts:trpzApUnconfiguredMib.setRevisions(('2011-06-15 00:11','2008-11-14 00:04'))
class TrpzApUnconfiguredOrphanReason(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('other',1),('no-configuration',2),('ap-license-exceeded',3),('controller-behind-nat',4),('ap-model-mismatch',5),('no-macs',6)))
_TrpzApUnconfMibObjects_ObjectIdentity=ObjectIdentity
trpzApUnconfMibObjects=_TrpzApUnconfMibObjects_ObjectIdentity((1,3,6,1,4,1,14525,4,15,1))
_TrpzApUnconfOrphanTable_Object=MibTable
trpzApUnconfOrphanTable=_TrpzApUnconfOrphanTable_Object((1,3,6,1,4,1,14525,4,15,1,2))
if mibBuilder.loadTexts:trpzApUnconfOrphanTable.setStatus(_A)
_TrpzApUnconfOrphanEntry_Object=MibTableRow
trpzApUnconfOrphanEntry=_TrpzApUnconfOrphanEntry_Object((1,3,6,1,4,1,14525,4,15,1,2,1))
trpzApUnconfOrphanEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:trpzApUnconfOrphanEntry.setStatus(_A)
_TrpzApUnconfOrphanApSerialNum_Type=TrpzApSerialNum
_TrpzApUnconfOrphanApSerialNum_Object=MibTableColumn
trpzApUnconfOrphanApSerialNum=_TrpzApUnconfOrphanApSerialNum_Object((1,3,6,1,4,1,14525,4,15,1,2,1,1),_TrpzApUnconfOrphanApSerialNum_Type())
trpzApUnconfOrphanApSerialNum.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:trpzApUnconfOrphanApSerialNum.setStatus(_A)
class _TrpzApUnconfOrphanApModelName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_TrpzApUnconfOrphanApModelName_Type.__name__=_D
_TrpzApUnconfOrphanApModelName_Object=MibTableColumn
trpzApUnconfOrphanApModelName=_TrpzApUnconfOrphanApModelName_Object((1,3,6,1,4,1,14525,4,15,1,2,1,2),_TrpzApUnconfOrphanApModelName_Type())
trpzApUnconfOrphanApModelName.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzApUnconfOrphanApModelName.setStatus(_A)
_TrpzApUnconfOrphanIpAddress_Type=IpAddress
_TrpzApUnconfOrphanIpAddress_Object=MibTableColumn
trpzApUnconfOrphanIpAddress=_TrpzApUnconfOrphanIpAddress_Object((1,3,6,1,4,1,14525,4,15,1,2,1,5),_TrpzApUnconfOrphanIpAddress_Type())
trpzApUnconfOrphanIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzApUnconfOrphanIpAddress.setStatus(_A)
_TrpzApUnconfOrphanPhysPortNum_Type=TrpzPhysPortNumber
_TrpzApUnconfOrphanPhysPortNum_Object=MibTableColumn
trpzApUnconfOrphanPhysPortNum=_TrpzApUnconfOrphanPhysPortNum_Object((1,3,6,1,4,1,14525,4,15,1,2,1,6),_TrpzApUnconfOrphanPhysPortNum_Type())
trpzApUnconfOrphanPhysPortNum.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzApUnconfOrphanPhysPortNum.setStatus(_A)
class _TrpzApUnconfOrphanVLANName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_TrpzApUnconfOrphanVLANName_Type.__name__=_D
_TrpzApUnconfOrphanVLANName_Object=MibTableColumn
trpzApUnconfOrphanVLANName=_TrpzApUnconfOrphanVLANName_Object((1,3,6,1,4,1,14525,4,15,1,2,1,7),_TrpzApUnconfOrphanVLANName_Type())
trpzApUnconfOrphanVLANName.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzApUnconfOrphanVLANName.setStatus(_A)
_TrpzApUnconfOrphanReason_Type=TrpzApUnconfiguredOrphanReason
_TrpzApUnconfOrphanReason_Object=MibTableColumn
trpzApUnconfOrphanReason=_TrpzApUnconfOrphanReason_Object((1,3,6,1,4,1,14525,4,15,1,2,1,8),_TrpzApUnconfOrphanReason_Type())
trpzApUnconfOrphanReason.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzApUnconfOrphanReason.setStatus(_A)
_TrpzApUnconfConformance_ObjectIdentity=ObjectIdentity
trpzApUnconfConformance=_TrpzApUnconfConformance_ObjectIdentity((1,3,6,1,4,1,14525,4,15,2))
_TrpzApUnconfCompliances_ObjectIdentity=ObjectIdentity
trpzApUnconfCompliances=_TrpzApUnconfCompliances_ObjectIdentity((1,3,6,1,4,1,14525,4,15,2,1))
_TrpzApUnconfGroups_ObjectIdentity=ObjectIdentity
trpzApUnconfGroups=_TrpzApUnconfGroups_ObjectIdentity((1,3,6,1,4,1,14525,4,15,2,2))
trpzApUnconfOrphanBasicGroup=ObjectGroup((1,3,6,1,4,1,14525,4,15,2,2,1))
trpzApUnconfOrphanBasicGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:trpzApUnconfOrphanBasicGroup.setStatus(_A)
trpzApUnconfCompliance=ModuleCompliance((1,3,6,1,4,1,14525,4,15,2,1,1))
trpzApUnconfCompliance.setObjects((_B,_K))
if mibBuilder.loadTexts:trpzApUnconfCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'TrpzApUnconfiguredOrphanReason':TrpzApUnconfiguredOrphanReason,'trpzApUnconfiguredMib':trpzApUnconfiguredMib,'trpzApUnconfMibObjects':trpzApUnconfMibObjects,'trpzApUnconfOrphanTable':trpzApUnconfOrphanTable,'trpzApUnconfOrphanEntry':trpzApUnconfOrphanEntry,_E:trpzApUnconfOrphanApSerialNum,_F:trpzApUnconfOrphanApModelName,_G:trpzApUnconfOrphanIpAddress,_H:trpzApUnconfOrphanPhysPortNum,_I:trpzApUnconfOrphanVLANName,_J:trpzApUnconfOrphanReason,'trpzApUnconfConformance':trpzApUnconfConformance,'trpzApUnconfCompliances':trpzApUnconfCompliances,'trpzApUnconfCompliance':trpzApUnconfCompliance,'trpzApUnconfGroups':trpzApUnconfGroups,_K:trpzApUnconfOrphanBasicGroup})