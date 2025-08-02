_U='acdVSetConfigGroup'
_T='acdVSetConfigOuterVlanID'
_S='acdVSetConfigOuterVlanType'
_R='acdVSetConfigVlanIDs3072to4095'
_Q='acdVSetConfigVlanIDs2048to3071'
_P='acdVSetConfigVlanIDs1024to2047'
_O='acdVSetConfigVlanIDs0to1023'
_N='acdVSetConfigVlanType'
_M='acdVSetConfigName'
_L='acdVSetConfigRowStatus'
_K='AcdVsetOuterVlanType'
_J='AcdVsetVlanType'
_I='not-accessible'
_H='acdVSetConfigID'
_G='acdVSetConfigPolicyListID'
_F='DisplayString'
_E='Unsigned32'
_D='OctetString'
_C='read-create'
_B='ACD-VSET-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
acdMibs,=mibBuilder.importSymbols('ACCEDIAN-SMI','acdMibs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','RowStatus','TextualConvention')
acdVSet=ModuleIdentity((1,3,6,1,4,1,22420,2,13))
if mibBuilder.loadTexts:acdVSet.setRevisions(('2015-05-05 01:00','2013-04-04 01:00','2013-02-13 01:00','2012-01-11 01:00'))
class AcdVsetVlanType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('cvlan',1),('svlan',2),('tvlan',3)))
class AcdVsetOuterVlanType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('cvlan',1),('svlan',2),('tvlan',3)))
_AcdVSetNotifications_ObjectIdentity=ObjectIdentity
acdVSetNotifications=_AcdVSetNotifications_ObjectIdentity((1,3,6,1,4,1,22420,2,13,0))
_AcdVSetMIBObjects_ObjectIdentity=ObjectIdentity
acdVSetMIBObjects=_AcdVSetMIBObjects_ObjectIdentity((1,3,6,1,4,1,22420,2,13,1))
_AcdVSetConfig_ObjectIdentity=ObjectIdentity
acdVSetConfig=_AcdVSetConfig_ObjectIdentity((1,3,6,1,4,1,22420,2,13,1,1))
_AcdVSetConfigTable_Object=MibTable
acdVSetConfigTable=_AcdVSetConfigTable_Object((1,3,6,1,4,1,22420,2,13,1,1,1))
if mibBuilder.loadTexts:acdVSetConfigTable.setStatus(_A)
_AcdVSetConfigEntry_Object=MibTableRow
acdVSetConfigEntry=_AcdVSetConfigEntry_Object((1,3,6,1,4,1,22420,2,13,1,1,1,1))
acdVSetConfigEntry.setIndexNames((0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:acdVSetConfigEntry.setStatus(_A)
_AcdVSetConfigPolicyListID_Type=Unsigned32
_AcdVSetConfigPolicyListID_Object=MibTableColumn
acdVSetConfigPolicyListID=_AcdVSetConfigPolicyListID_Object((1,3,6,1,4,1,22420,2,13,1,1,1,1,1),_AcdVSetConfigPolicyListID_Type())
acdVSetConfigPolicyListID.setMaxAccess(_I)
if mibBuilder.loadTexts:acdVSetConfigPolicyListID.setStatus(_A)
_AcdVSetConfigID_Type=Unsigned32
_AcdVSetConfigID_Object=MibTableColumn
acdVSetConfigID=_AcdVSetConfigID_Object((1,3,6,1,4,1,22420,2,13,1,1,1,1,2),_AcdVSetConfigID_Type())
acdVSetConfigID.setMaxAccess(_I)
if mibBuilder.loadTexts:acdVSetConfigID.setStatus(_A)
_AcdVSetConfigRowStatus_Type=RowStatus
_AcdVSetConfigRowStatus_Object=MibTableColumn
acdVSetConfigRowStatus=_AcdVSetConfigRowStatus_Object((1,3,6,1,4,1,22420,2,13,1,1,1,1,3),_AcdVSetConfigRowStatus_Type())
acdVSetConfigRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:acdVSetConfigRowStatus.setStatus(_A)
class _AcdVSetConfigName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AcdVSetConfigName_Type.__name__=_F
_AcdVSetConfigName_Object=MibTableColumn
acdVSetConfigName=_AcdVSetConfigName_Object((1,3,6,1,4,1,22420,2,13,1,1,1,1,4),_AcdVSetConfigName_Type())
acdVSetConfigName.setMaxAccess(_C)
if mibBuilder.loadTexts:acdVSetConfigName.setStatus(_A)
class _AcdVSetConfigVlanType_Type(AcdVsetVlanType):defaultValue=1
_AcdVSetConfigVlanType_Type.__name__=_J
_AcdVSetConfigVlanType_Object=MibTableColumn
acdVSetConfigVlanType=_AcdVSetConfigVlanType_Object((1,3,6,1,4,1,22420,2,13,1,1,1,1,5),_AcdVSetConfigVlanType_Type())
acdVSetConfigVlanType.setMaxAccess(_C)
if mibBuilder.loadTexts:acdVSetConfigVlanType.setStatus(_A)
class _AcdVSetConfigVlanIDs0to1023_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_AcdVSetConfigVlanIDs0to1023_Type.__name__=_D
_AcdVSetConfigVlanIDs0to1023_Object=MibTableColumn
acdVSetConfigVlanIDs0to1023=_AcdVSetConfigVlanIDs0to1023_Object((1,3,6,1,4,1,22420,2,13,1,1,1,1,6),_AcdVSetConfigVlanIDs0to1023_Type())
acdVSetConfigVlanIDs0to1023.setMaxAccess(_C)
if mibBuilder.loadTexts:acdVSetConfigVlanIDs0to1023.setStatus(_A)
class _AcdVSetConfigVlanIDs1024to2047_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_AcdVSetConfigVlanIDs1024to2047_Type.__name__=_D
_AcdVSetConfigVlanIDs1024to2047_Object=MibTableColumn
acdVSetConfigVlanIDs1024to2047=_AcdVSetConfigVlanIDs1024to2047_Object((1,3,6,1,4,1,22420,2,13,1,1,1,1,7),_AcdVSetConfigVlanIDs1024to2047_Type())
acdVSetConfigVlanIDs1024to2047.setMaxAccess(_C)
if mibBuilder.loadTexts:acdVSetConfigVlanIDs1024to2047.setStatus(_A)
class _AcdVSetConfigVlanIDs2048to3071_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_AcdVSetConfigVlanIDs2048to3071_Type.__name__=_D
_AcdVSetConfigVlanIDs2048to3071_Object=MibTableColumn
acdVSetConfigVlanIDs2048to3071=_AcdVSetConfigVlanIDs2048to3071_Object((1,3,6,1,4,1,22420,2,13,1,1,1,1,8),_AcdVSetConfigVlanIDs2048to3071_Type())
acdVSetConfigVlanIDs2048to3071.setMaxAccess(_C)
if mibBuilder.loadTexts:acdVSetConfigVlanIDs2048to3071.setStatus(_A)
class _AcdVSetConfigVlanIDs3072to4095_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_AcdVSetConfigVlanIDs3072to4095_Type.__name__=_D
_AcdVSetConfigVlanIDs3072to4095_Object=MibTableColumn
acdVSetConfigVlanIDs3072to4095=_AcdVSetConfigVlanIDs3072to4095_Object((1,3,6,1,4,1,22420,2,13,1,1,1,1,9),_AcdVSetConfigVlanIDs3072to4095_Type())
acdVSetConfigVlanIDs3072to4095.setMaxAccess(_C)
if mibBuilder.loadTexts:acdVSetConfigVlanIDs3072to4095.setStatus(_A)
class _AcdVSetConfigOuterVlanType_Type(AcdVsetOuterVlanType):defaultValue=0
_AcdVSetConfigOuterVlanType_Type.__name__=_K
_AcdVSetConfigOuterVlanType_Object=MibTableColumn
acdVSetConfigOuterVlanType=_AcdVSetConfigOuterVlanType_Object((1,3,6,1,4,1,22420,2,13,1,1,1,1,10),_AcdVSetConfigOuterVlanType_Type())
acdVSetConfigOuterVlanType.setMaxAccess(_C)
if mibBuilder.loadTexts:acdVSetConfigOuterVlanType.setStatus(_A)
class _AcdVSetConfigOuterVlanID_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_AcdVSetConfigOuterVlanID_Type.__name__=_E
_AcdVSetConfigOuterVlanID_Object=MibTableColumn
acdVSetConfigOuterVlanID=_AcdVSetConfigOuterVlanID_Object((1,3,6,1,4,1,22420,2,13,1,1,1,1,11),_AcdVSetConfigOuterVlanID_Type())
acdVSetConfigOuterVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:acdVSetConfigOuterVlanID.setStatus(_A)
_AcdVSetConformance_ObjectIdentity=ObjectIdentity
acdVSetConformance=_AcdVSetConformance_ObjectIdentity((1,3,6,1,4,1,22420,2,13,2))
_AcdVSetCompliances_ObjectIdentity=ObjectIdentity
acdVSetCompliances=_AcdVSetCompliances_ObjectIdentity((1,3,6,1,4,1,22420,2,13,2,1))
_AcdVSetGroups_ObjectIdentity=ObjectIdentity
acdVSetGroups=_AcdVSetGroups_ObjectIdentity((1,3,6,1,4,1,22420,2,13,2,2))
acdVSetConfigGroup=ObjectGroup((1,3,6,1,4,1,22420,2,13,2,2,1))
acdVSetConfigGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:acdVSetConfigGroup.setStatus(_A)
acdVSetCompliance=ModuleCompliance((1,3,6,1,4,1,22420,2,13,2,1,1))
acdVSetCompliance.setObjects((_B,_U))
if mibBuilder.loadTexts:acdVSetCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_J:AcdVsetVlanType,_K:AcdVsetOuterVlanType,'acdVSet':acdVSet,'acdVSetNotifications':acdVSetNotifications,'acdVSetMIBObjects':acdVSetMIBObjects,'acdVSetConfig':acdVSetConfig,'acdVSetConfigTable':acdVSetConfigTable,'acdVSetConfigEntry':acdVSetConfigEntry,_G:acdVSetConfigPolicyListID,_H:acdVSetConfigID,_L:acdVSetConfigRowStatus,_M:acdVSetConfigName,_N:acdVSetConfigVlanType,_O:acdVSetConfigVlanIDs0to1023,_P:acdVSetConfigVlanIDs1024to2047,_Q:acdVSetConfigVlanIDs2048to3071,_R:acdVSetConfigVlanIDs3072to4095,_S:acdVSetConfigOuterVlanType,_T:acdVSetConfigOuterVlanID,'acdVSetConformance':acdVSetConformance,'acdVSetCompliances':acdVSetCompliances,'acdVSetCompliance':acdVSetCompliance,'acdVSetGroups':acdVSetGroups,_U:acdVSetConfigGroup})