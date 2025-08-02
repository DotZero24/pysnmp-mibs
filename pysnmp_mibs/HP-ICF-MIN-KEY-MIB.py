_H='hpicfMinKeyConfigGroup'
_G='hpicfMinKeyRowStatus'
_F='hpicfMinKeySize'
_E='read-create'
_D='hpicfMinKeyType'
_C='Integer32'
_B='HP-ICF-MIN-KEY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
hpicfMinKeyMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,132))
if mibBuilder.loadTexts:hpicfMinKeyMIB.setRevisions(('2016-06-22 09:00',))
_HpicfMinKeyObjects_ObjectIdentity=ObjectIdentity
hpicfMinKeyObjects=_HpicfMinKeyObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,132,0))
_HpicfMinKeyConfigObjects_ObjectIdentity=ObjectIdentity
hpicfMinKeyConfigObjects=_HpicfMinKeyConfigObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,132,0,1))
_HpicfMinKeyTable_Object=MibTable
hpicfMinKeyTable=_HpicfMinKeyTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,132,0,1,1))
if mibBuilder.loadTexts:hpicfMinKeyTable.setStatus(_A)
_HpicfMinKeyEntry_Object=MibTableRow
hpicfMinKeyEntry=_HpicfMinKeyEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,132,0,1,1,1))
hpicfMinKeyEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:hpicfMinKeyEntry.setStatus(_A)
class _HpicfMinKeyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('rsa',1))
_HpicfMinKeyType_Type.__name__=_C
_HpicfMinKeyType_Object=MibTableColumn
hpicfMinKeyType=_HpicfMinKeyType_Object((1,3,6,1,4,1,11,2,14,11,5,1,132,0,1,1,1,1),_HpicfMinKeyType_Type())
hpicfMinKeyType.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hpicfMinKeyType.setStatus(_A)
class _HpicfMinKeySize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('minBit1024',1),('minBit2048',2)))
_HpicfMinKeySize_Type.__name__=_C
_HpicfMinKeySize_Object=MibTableColumn
hpicfMinKeySize=_HpicfMinKeySize_Object((1,3,6,1,4,1,11,2,14,11,5,1,132,0,1,1,1,2),_HpicfMinKeySize_Type())
hpicfMinKeySize.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfMinKeySize.setStatus(_A)
_HpicfMinKeyRowStatus_Type=RowStatus
_HpicfMinKeyRowStatus_Object=MibTableColumn
hpicfMinKeyRowStatus=_HpicfMinKeyRowStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,132,0,1,1,1,3),_HpicfMinKeyRowStatus_Type())
hpicfMinKeyRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfMinKeyRowStatus.setStatus(_A)
_HpicfMinKeyConformance_ObjectIdentity=ObjectIdentity
hpicfMinKeyConformance=_HpicfMinKeyConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,132,1))
_HpicfMinKeyCompliances_ObjectIdentity=ObjectIdentity
hpicfMinKeyCompliances=_HpicfMinKeyCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,132,1,1))
_HpicfMinKeyGroups_ObjectIdentity=ObjectIdentity
hpicfMinKeyGroups=_HpicfMinKeyGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,132,1,2))
hpicfMinKeyConfigGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,132,1,2,1))
hpicfMinKeyConfigGroup.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:hpicfMinKeyConfigGroup.setStatus(_A)
hpicfMinKeyCompliance1=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,132,1,1,1))
hpicfMinKeyCompliance1.setObjects((_B,_H))
if mibBuilder.loadTexts:hpicfMinKeyCompliance1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpicfMinKeyMIB':hpicfMinKeyMIB,'hpicfMinKeyObjects':hpicfMinKeyObjects,'hpicfMinKeyConfigObjects':hpicfMinKeyConfigObjects,'hpicfMinKeyTable':hpicfMinKeyTable,'hpicfMinKeyEntry':hpicfMinKeyEntry,_D:hpicfMinKeyType,_F:hpicfMinKeySize,_G:hpicfMinKeyRowStatus,'hpicfMinKeyConformance':hpicfMinKeyConformance,'hpicfMinKeyCompliances':hpicfMinKeyCompliances,'hpicfMinKeyCompliance1':hpicfMinKeyCompliance1,'hpicfMinKeyGroups':hpicfMinKeyGroups,_H:hpicfMinKeyConfigGroup})