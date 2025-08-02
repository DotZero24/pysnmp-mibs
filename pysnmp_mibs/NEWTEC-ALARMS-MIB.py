_K='ntcAlmsConfGrpV1Standard'
_J='ntcAlmsConfigGeneralDevice'
_I='ntcAlmsConfigGeneralInterface'
_H='ntcAlmsConfigMask'
_G='ntcAlmsConfigName'
_F='DisplayString'
_E='read-write'
_D='off'
_C='Integer32'
_B='NEWTEC-ALARMS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ntcFunction,=mibBuilder.importSymbols('NEWTEC-MAIN-MIB','ntcFunction')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
ntcAlarms=ModuleIdentity((1,3,6,1,4,1,5835,5,2,5600))
if mibBuilder.loadTexts:ntcAlarms.setRevisions(('2013-09-20 10:00','2013-09-20 08:00'))
_NtcAlmsObjects_ObjectIdentity=ObjectIdentity
ntcAlmsObjects=_NtcAlmsObjects_ObjectIdentity((1,3,6,1,4,1,5835,5,2,5600,1))
if mibBuilder.loadTexts:ntcAlmsObjects.setStatus(_A)
_NtcAlmsConfigTable_Object=MibTable
ntcAlmsConfigTable=_NtcAlmsConfigTable_Object((1,3,6,1,4,1,5835,5,2,5600,1,1))
if mibBuilder.loadTexts:ntcAlmsConfigTable.setStatus(_A)
_NtcAlmsConfigEntry_Object=MibTableRow
ntcAlmsConfigEntry=_NtcAlmsConfigEntry_Object((1,3,6,1,4,1,5835,5,2,5600,1,1,1))
ntcAlmsConfigEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:ntcAlmsConfigEntry.setStatus(_A)
class _NtcAlmsConfigName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_NtcAlmsConfigName_Type.__name__=_F
_NtcAlmsConfigName_Object=MibTableColumn
ntcAlmsConfigName=_NtcAlmsConfigName_Object((1,3,6,1,4,1,5835,5,2,5600,1,1,1,1),_NtcAlmsConfigName_Type())
ntcAlmsConfigName.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ntcAlmsConfigName.setStatus(_A)
class _NtcAlmsConfigMask_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),('on',1)))
_NtcAlmsConfigMask_Type.__name__=_C
_NtcAlmsConfigMask_Object=MibTableColumn
ntcAlmsConfigMask=_NtcAlmsConfigMask_Object((1,3,6,1,4,1,5835,5,2,5600,1,1,1,2),_NtcAlmsConfigMask_Type())
ntcAlmsConfigMask.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcAlmsConfigMask.setStatus(_A)
class _NtcAlmsConfigGeneralInterface_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),('on',1)))
_NtcAlmsConfigGeneralInterface_Type.__name__=_C
_NtcAlmsConfigGeneralInterface_Object=MibTableColumn
ntcAlmsConfigGeneralInterface=_NtcAlmsConfigGeneralInterface_Object((1,3,6,1,4,1,5835,5,2,5600,1,1,1,3),_NtcAlmsConfigGeneralInterface_Type())
ntcAlmsConfigGeneralInterface.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcAlmsConfigGeneralInterface.setStatus(_A)
class _NtcAlmsConfigGeneralDevice_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),('on',1)))
_NtcAlmsConfigGeneralDevice_Type.__name__=_C
_NtcAlmsConfigGeneralDevice_Object=MibTableColumn
ntcAlmsConfigGeneralDevice=_NtcAlmsConfigGeneralDevice_Object((1,3,6,1,4,1,5835,5,2,5600,1,1,1,4),_NtcAlmsConfigGeneralDevice_Type())
ntcAlmsConfigGeneralDevice.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcAlmsConfigGeneralDevice.setStatus(_A)
_NtcAlmsConformance_ObjectIdentity=ObjectIdentity
ntcAlmsConformance=_NtcAlmsConformance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,5600,2))
if mibBuilder.loadTexts:ntcAlmsConformance.setStatus(_A)
_NtcAlmsConfCompliance_ObjectIdentity=ObjectIdentity
ntcAlmsConfCompliance=_NtcAlmsConfCompliance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,5600,2,1))
if mibBuilder.loadTexts:ntcAlmsConfCompliance.setStatus(_A)
_NtcAlmsConfGroup_ObjectIdentity=ObjectIdentity
ntcAlmsConfGroup=_NtcAlmsConfGroup_ObjectIdentity((1,3,6,1,4,1,5835,5,2,5600,2,2))
if mibBuilder.loadTexts:ntcAlmsConfGroup.setStatus(_A)
ntcAlmsConfGrpV1Standard=ObjectGroup((1,3,6,1,4,1,5835,5,2,5600,2,2,1))
ntcAlmsConfGrpV1Standard.setObjects(*((_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:ntcAlmsConfGrpV1Standard.setStatus(_A)
ntcAlmsConfCompV1Standard=ModuleCompliance((1,3,6,1,4,1,5835,5,2,5600,2,1,1))
ntcAlmsConfCompV1Standard.setObjects((_B,_K))
if mibBuilder.loadTexts:ntcAlmsConfCompV1Standard.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ntcAlarms':ntcAlarms,'ntcAlmsObjects':ntcAlmsObjects,'ntcAlmsConfigTable':ntcAlmsConfigTable,'ntcAlmsConfigEntry':ntcAlmsConfigEntry,_G:ntcAlmsConfigName,_H:ntcAlmsConfigMask,_I:ntcAlmsConfigGeneralInterface,_J:ntcAlmsConfigGeneralDevice,'ntcAlmsConformance':ntcAlmsConformance,'ntcAlmsConfCompliance':ntcAlmsConfCompliance,'ntcAlmsConfCompV1Standard':ntcAlmsConfCompV1Standard,'ntcAlmsConfGroup':ntcAlmsConfGroup,_K:ntcAlmsConfGrpV1Standard})