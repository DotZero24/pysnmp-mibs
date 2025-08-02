_U='hpicfDeviceIdentityGroup2'
_T='hpicfDeviceIdentityGroup1'
_S='hpicfDeviceIdentityGroup'
_R='hpicfDeviceIdentityLldpSysDescr'
_Q='hpicfDeviceIdentityLldpSysName'
_P='hpicfDevIdentityCdpType'
_O='not-accessible'
_N='Unsigned32'
_M='hpicfDevIdentityCdpRowStatus'
_L='hpicfDevIdentityCdpValue'
_K='hpicfDeviceIdentityIndex'
_J='Integer32'
_I='deprecated'
_H='hpicfDeviceIdentityLldpSubType'
_G='hpicfDeviceIdentityLldpOui'
_F='hpicfDeviceIdentityName'
_E='hpicfDeviceIdentityRowStatus'
_D='OctetString'
_C='read-create'
_B='current'
_A='HP-ICF-DEVICEIDENTITY-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_N,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
hpicfDeviceIdentityMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,135))
if mibBuilder.loadTexts:hpicfDeviceIdentityMIB.setRevisions(('2019-07-16 00:00','2017-12-05 00:00','2017-01-03 00:00'))
_HpicfDeviceIdentityConfig_ObjectIdentity=ObjectIdentity
hpicfDeviceIdentityConfig=_HpicfDeviceIdentityConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,135,1))
_HpicfDeviceIdentityTable_Object=MibTable
hpicfDeviceIdentityTable=_HpicfDeviceIdentityTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,135,1,1))
if mibBuilder.loadTexts:hpicfDeviceIdentityTable.setStatus(_B)
_HpicfDeviceIdentityEntry_Object=MibTableRow
hpicfDeviceIdentityEntry=_HpicfDeviceIdentityEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,135,1,1,1))
hpicfDeviceIdentityEntry.setIndexNames((0,_A,_K))
if mibBuilder.loadTexts:hpicfDeviceIdentityEntry.setStatus(_B)
class _HpicfDeviceIdentityIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_HpicfDeviceIdentityIndex_Type.__name__=_N
_HpicfDeviceIdentityIndex_Object=MibTableColumn
hpicfDeviceIdentityIndex=_HpicfDeviceIdentityIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,135,1,1,1,1),_HpicfDeviceIdentityIndex_Type())
hpicfDeviceIdentityIndex.setMaxAccess(_O)
if mibBuilder.loadTexts:hpicfDeviceIdentityIndex.setStatus(_B)
_HpicfDeviceIdentityRowStatus_Type=RowStatus
_HpicfDeviceIdentityRowStatus_Object=MibTableColumn
hpicfDeviceIdentityRowStatus=_HpicfDeviceIdentityRowStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,135,1,1,1,2),_HpicfDeviceIdentityRowStatus_Type())
hpicfDeviceIdentityRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDeviceIdentityRowStatus.setStatus(_B)
class _HpicfDeviceIdentityName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_HpicfDeviceIdentityName_Type.__name__=_D
_HpicfDeviceIdentityName_Object=MibTableColumn
hpicfDeviceIdentityName=_HpicfDeviceIdentityName_Object((1,3,6,1,4,1,11,2,14,11,5,1,135,1,1,1,3),_HpicfDeviceIdentityName_Type())
hpicfDeviceIdentityName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDeviceIdentityName.setStatus(_B)
class _HpicfDeviceIdentityLldpOui_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_HpicfDeviceIdentityLldpOui_Type.__name__=_D
_HpicfDeviceIdentityLldpOui_Object=MibTableColumn
hpicfDeviceIdentityLldpOui=_HpicfDeviceIdentityLldpOui_Object((1,3,6,1,4,1,11,2,14,11,5,1,135,1,1,1,4),_HpicfDeviceIdentityLldpOui_Type())
hpicfDeviceIdentityLldpOui.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDeviceIdentityLldpOui.setStatus(_B)
class _HpicfDeviceIdentityLldpSubType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpicfDeviceIdentityLldpSubType_Type.__name__=_J
_HpicfDeviceIdentityLldpSubType_Object=MibTableColumn
hpicfDeviceIdentityLldpSubType=_HpicfDeviceIdentityLldpSubType_Object((1,3,6,1,4,1,11,2,14,11,5,1,135,1,1,1,5),_HpicfDeviceIdentityLldpSubType_Type())
hpicfDeviceIdentityLldpSubType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDeviceIdentityLldpSubType.setStatus(_B)
class _HpicfDeviceIdentityLldpSysName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,512))
_HpicfDeviceIdentityLldpSysName_Type.__name__=_D
_HpicfDeviceIdentityLldpSysName_Object=MibTableColumn
hpicfDeviceIdentityLldpSysName=_HpicfDeviceIdentityLldpSysName_Object((1,3,6,1,4,1,11,2,14,11,5,1,135,1,1,1,6),_HpicfDeviceIdentityLldpSysName_Type())
hpicfDeviceIdentityLldpSysName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDeviceIdentityLldpSysName.setStatus(_B)
class _HpicfDeviceIdentityLldpSysDescr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,512))
_HpicfDeviceIdentityLldpSysDescr_Type.__name__=_D
_HpicfDeviceIdentityLldpSysDescr_Object=MibTableColumn
hpicfDeviceIdentityLldpSysDescr=_HpicfDeviceIdentityLldpSysDescr_Object((1,3,6,1,4,1,11,2,14,11,5,1,135,1,1,1,7),_HpicfDeviceIdentityLldpSysDescr_Type())
hpicfDeviceIdentityLldpSysDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDeviceIdentityLldpSysDescr.setStatus(_B)
_HpicfCdpBypassTable_Object=MibTable
hpicfCdpBypassTable=_HpicfCdpBypassTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,135,1,2))
if mibBuilder.loadTexts:hpicfCdpBypassTable.setStatus(_B)
_HpicfCdpBypassEntry_Object=MibTableRow
hpicfCdpBypassEntry=_HpicfCdpBypassEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,135,1,2,1))
hpicfCdpBypassEntry.setIndexNames((0,_A,_K),(0,_A,_P))
if mibBuilder.loadTexts:hpicfCdpBypassEntry.setStatus(_B)
class _HpicfDevIdentityCdpType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,19))
_HpicfDevIdentityCdpType_Type.__name__=_J
_HpicfDevIdentityCdpType_Object=MibTableColumn
hpicfDevIdentityCdpType=_HpicfDevIdentityCdpType_Object((1,3,6,1,4,1,11,2,14,11,5,1,135,1,2,1,1),_HpicfDevIdentityCdpType_Type())
hpicfDevIdentityCdpType.setMaxAccess(_O)
if mibBuilder.loadTexts:hpicfDevIdentityCdpType.setStatus(_B)
class _HpicfDevIdentityCdpValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpicfDevIdentityCdpValue_Type.__name__=_D
_HpicfDevIdentityCdpValue_Object=MibTableColumn
hpicfDevIdentityCdpValue=_HpicfDevIdentityCdpValue_Object((1,3,6,1,4,1,11,2,14,11,5,1,135,1,2,1,2),_HpicfDevIdentityCdpValue_Type())
hpicfDevIdentityCdpValue.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDevIdentityCdpValue.setStatus(_B)
_HpicfDevIdentityCdpRowStatus_Type=RowStatus
_HpicfDevIdentityCdpRowStatus_Object=MibTableColumn
hpicfDevIdentityCdpRowStatus=_HpicfDevIdentityCdpRowStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,135,1,2,1,3),_HpicfDevIdentityCdpRowStatus_Type())
hpicfDevIdentityCdpRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDevIdentityCdpRowStatus.setStatus(_B)
_HpicfDeviceIdentityConformance_ObjectIdentity=ObjectIdentity
hpicfDeviceIdentityConformance=_HpicfDeviceIdentityConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,135,2))
_HpicfDeviceIdentityGroups_ObjectIdentity=ObjectIdentity
hpicfDeviceIdentityGroups=_HpicfDeviceIdentityGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,135,2,1))
_HpicfDeviceIdentityCompliances_ObjectIdentity=ObjectIdentity
hpicfDeviceIdentityCompliances=_HpicfDeviceIdentityCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,135,2,2))
hpicfDeviceIdentityGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,135,2,1,1))
hpicfDeviceIdentityGroup.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:hpicfDeviceIdentityGroup.setStatus(_I)
hpicfDeviceIdentityGroup1=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,135,2,1,2))
hpicfDeviceIdentityGroup1.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:hpicfDeviceIdentityGroup1.setStatus(_I)
hpicfDeviceIdentityGroup2=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,135,2,1,3))
hpicfDeviceIdentityGroup2.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_Q),(_A,_R),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:hpicfDeviceIdentityGroup2.setStatus(_B)
hpicfiDeviceIdentityCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,135,2,2,1))
hpicfiDeviceIdentityCompliance.setObjects((_A,_S))
if mibBuilder.loadTexts:hpicfiDeviceIdentityCompliance.setStatus(_I)
hpicfiDeviceIdentityCompliance1=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,135,2,2,2))
hpicfiDeviceIdentityCompliance1.setObjects((_A,_T))
if mibBuilder.loadTexts:hpicfiDeviceIdentityCompliance1.setStatus(_I)
hpicfDeviceIdentityCompliance2=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,135,2,2,3))
hpicfDeviceIdentityCompliance2.setObjects((_A,_U))
if mibBuilder.loadTexts:hpicfDeviceIdentityCompliance2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'hpicfDeviceIdentityMIB':hpicfDeviceIdentityMIB,'hpicfDeviceIdentityConfig':hpicfDeviceIdentityConfig,'hpicfDeviceIdentityTable':hpicfDeviceIdentityTable,'hpicfDeviceIdentityEntry':hpicfDeviceIdentityEntry,_K:hpicfDeviceIdentityIndex,_E:hpicfDeviceIdentityRowStatus,_F:hpicfDeviceIdentityName,_G:hpicfDeviceIdentityLldpOui,_H:hpicfDeviceIdentityLldpSubType,_Q:hpicfDeviceIdentityLldpSysName,_R:hpicfDeviceIdentityLldpSysDescr,'hpicfCdpBypassTable':hpicfCdpBypassTable,'hpicfCdpBypassEntry':hpicfCdpBypassEntry,_P:hpicfDevIdentityCdpType,_L:hpicfDevIdentityCdpValue,_M:hpicfDevIdentityCdpRowStatus,'hpicfDeviceIdentityConformance':hpicfDeviceIdentityConformance,'hpicfDeviceIdentityGroups':hpicfDeviceIdentityGroups,_S:hpicfDeviceIdentityGroup,_T:hpicfDeviceIdentityGroup1,_U:hpicfDeviceIdentityGroup2,'hpicfDeviceIdentityCompliances':hpicfDeviceIdentityCompliances,'hpicfiDeviceIdentityCompliance':hpicfiDeviceIdentityCompliance,'hpicfiDeviceIdentityCompliance1':hpicfiDeviceIdentityCompliance1,'hpicfDeviceIdentityCompliance2':hpicfDeviceIdentityCompliance2})