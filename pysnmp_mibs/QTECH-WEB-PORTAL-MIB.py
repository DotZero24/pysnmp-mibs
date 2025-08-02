_h='qtechWebPortalMIBGroup'
_g='qtechWebPortalEntryStatus'
_f='qtechWebPortalWebPageTitle'
_e='qtechWebPortalWelcomeMsg'
_d='qtechWebPortalEchoManufacturerLogo'
_c='qtechWebPortalCustomizedLogoName'
_b='qtechWebPortalExtWebPortalURL'
_a='qtechWebPortalCustomizedPageName'
_Z='qtechWebPortalMetholdList'
_Y='qtechWebPortalUseGlbConfigFlag'
_X='qtechWebPortalWebAuthType'
_W='qtechWebPortalGlbWebPageTitle'
_V='qtechWebPortalGlbWelcomeMsg'
_U='qtechWebPortalGlbEchoManufacturerLogo'
_T='qtechWebPortalGlbCustomizedLogoName'
_S='qtechWebPortalGlbExternalWebPortalURL'
_R='qtechWebPortalGlbCustomizedPageName'
_Q='qtechWebPortalGlbMethodList'
_P='qtechWebPortalGlbWebAuthType'
_O='read-only'
_N='external'
_M='customized'
_L='internal'
_K='qtechWebPortalNetID'
_J='qtechWebPortalNetMode'
_I='enable'
_H='disable'
_G='OctetString'
_F='read-write'
_E='Integer32'
_D='read-create'
_C='DisplayString'
_B='QTECH-WEB-PORTAL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','RowStatus','TextualConvention')
qtechWebPortalMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,69))
if mibBuilder.loadTexts:qtechWebPortalMIB.setRevisions(('2010-02-02 00:00',))
_QtechWebPortalMIBObjects_ObjectIdentity=ObjectIdentity
qtechWebPortalMIBObjects=_QtechWebPortalMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,69,1))
_QtechWebPortalGlobalMIBObjects_ObjectIdentity=ObjectIdentity
qtechWebPortalGlobalMIBObjects=_QtechWebPortalGlobalMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,69,1,1))
class _QtechWebPortalGlbWebAuthType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_L,0),(_M,1),(_N,2)))
_QtechWebPortalGlbWebAuthType_Type.__name__=_E
_QtechWebPortalGlbWebAuthType_Object=MibScalar
qtechWebPortalGlbWebAuthType=_QtechWebPortalGlbWebAuthType_Object((1,3,6,1,4,1,27514,1,1,10,2,69,1,1,1),_QtechWebPortalGlbWebAuthType_Type())
qtechWebPortalGlbWebAuthType.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechWebPortalGlbWebAuthType.setStatus(_A)
class _QtechWebPortalGlbMethodList_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,63))
_QtechWebPortalGlbMethodList_Type.__name__=_C
_QtechWebPortalGlbMethodList_Object=MibScalar
qtechWebPortalGlbMethodList=_QtechWebPortalGlbMethodList_Object((1,3,6,1,4,1,27514,1,1,10,2,69,1,1,2),_QtechWebPortalGlbMethodList_Type())
qtechWebPortalGlbMethodList.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechWebPortalGlbMethodList.setStatus(_A)
class _QtechWebPortalGlbCustomizedPageName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,130))
_QtechWebPortalGlbCustomizedPageName_Type.__name__=_C
_QtechWebPortalGlbCustomizedPageName_Object=MibScalar
qtechWebPortalGlbCustomizedPageName=_QtechWebPortalGlbCustomizedPageName_Object((1,3,6,1,4,1,27514,1,1,10,2,69,1,1,3),_QtechWebPortalGlbCustomizedPageName_Type())
qtechWebPortalGlbCustomizedPageName.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechWebPortalGlbCustomizedPageName.setStatus(_A)
class _QtechWebPortalGlbExternalWebPortalURL_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,130))
_QtechWebPortalGlbExternalWebPortalURL_Type.__name__=_C
_QtechWebPortalGlbExternalWebPortalURL_Object=MibScalar
qtechWebPortalGlbExternalWebPortalURL=_QtechWebPortalGlbExternalWebPortalURL_Object((1,3,6,1,4,1,27514,1,1,10,2,69,1,1,4),_QtechWebPortalGlbExternalWebPortalURL_Type())
qtechWebPortalGlbExternalWebPortalURL.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechWebPortalGlbExternalWebPortalURL.setStatus(_A)
class _QtechWebPortalGlbCustomizedLogoName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,130))
_QtechWebPortalGlbCustomizedLogoName_Type.__name__=_C
_QtechWebPortalGlbCustomizedLogoName_Object=MibScalar
qtechWebPortalGlbCustomizedLogoName=_QtechWebPortalGlbCustomizedLogoName_Object((1,3,6,1,4,1,27514,1,1,10,2,69,1,1,5),_QtechWebPortalGlbCustomizedLogoName_Type())
qtechWebPortalGlbCustomizedLogoName.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechWebPortalGlbCustomizedLogoName.setStatus(_A)
class _QtechWebPortalGlbEchoManufacturerLogo_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_QtechWebPortalGlbEchoManufacturerLogo_Type.__name__=_E
_QtechWebPortalGlbEchoManufacturerLogo_Object=MibScalar
qtechWebPortalGlbEchoManufacturerLogo=_QtechWebPortalGlbEchoManufacturerLogo_Object((1,3,6,1,4,1,27514,1,1,10,2,69,1,1,6),_QtechWebPortalGlbEchoManufacturerLogo_Type())
qtechWebPortalGlbEchoManufacturerLogo.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechWebPortalGlbEchoManufacturerLogo.setStatus(_A)
class _QtechWebPortalGlbWelcomeMsg_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,2047))
_QtechWebPortalGlbWelcomeMsg_Type.__name__=_G
_QtechWebPortalGlbWelcomeMsg_Object=MibScalar
qtechWebPortalGlbWelcomeMsg=_QtechWebPortalGlbWelcomeMsg_Object((1,3,6,1,4,1,27514,1,1,10,2,69,1,1,7),_QtechWebPortalGlbWelcomeMsg_Type())
qtechWebPortalGlbWelcomeMsg.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechWebPortalGlbWelcomeMsg.setStatus(_A)
class _QtechWebPortalGlbWebPageTitle_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,130))
_QtechWebPortalGlbWebPageTitle_Type.__name__=_C
_QtechWebPortalGlbWebPageTitle_Object=MibScalar
qtechWebPortalGlbWebPageTitle=_QtechWebPortalGlbWebPageTitle_Object((1,3,6,1,4,1,27514,1,1,10,2,69,1,1,8),_QtechWebPortalGlbWebPageTitle_Type())
qtechWebPortalGlbWebPageTitle.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechWebPortalGlbWebPageTitle.setStatus(_A)
_QtechWebPortalLocalMIBObjects_ObjectIdentity=ObjectIdentity
qtechWebPortalLocalMIBObjects=_QtechWebPortalLocalMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,69,1,2))
_QtechWebPortalAuthTable_Object=MibTable
qtechWebPortalAuthTable=_QtechWebPortalAuthTable_Object((1,3,6,1,4,1,27514,1,1,10,2,69,1,2,1))
if mibBuilder.loadTexts:qtechWebPortalAuthTable.setStatus(_A)
_QtechWebPortalAuthEntry_Object=MibTableRow
qtechWebPortalAuthEntry=_QtechWebPortalAuthEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,69,1,2,1,1))
qtechWebPortalAuthEntry.setIndexNames((0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:qtechWebPortalAuthEntry.setStatus(_A)
class _QtechWebPortalNetMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('wlan',1),('ethernet',2),('vlan',3)))
_QtechWebPortalNetMode_Type.__name__=_E
_QtechWebPortalNetMode_Object=MibTableColumn
qtechWebPortalNetMode=_QtechWebPortalNetMode_Object((1,3,6,1,4,1,27514,1,1,10,2,69,1,2,1,1,1),_QtechWebPortalNetMode_Type())
qtechWebPortalNetMode.setMaxAccess(_O)
if mibBuilder.loadTexts:qtechWebPortalNetMode.setStatus(_A)
class _QtechWebPortalNetID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_QtechWebPortalNetID_Type.__name__=_E
_QtechWebPortalNetID_Object=MibTableColumn
qtechWebPortalNetID=_QtechWebPortalNetID_Object((1,3,6,1,4,1,27514,1,1,10,2,69,1,2,1,1,2),_QtechWebPortalNetID_Type())
qtechWebPortalNetID.setMaxAccess(_O)
if mibBuilder.loadTexts:qtechWebPortalNetID.setStatus(_A)
class _QtechWebPortalWebAuthType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_L,0),(_M,1),(_N,2)))
_QtechWebPortalWebAuthType_Type.__name__=_E
_QtechWebPortalWebAuthType_Object=MibTableColumn
qtechWebPortalWebAuthType=_QtechWebPortalWebAuthType_Object((1,3,6,1,4,1,27514,1,1,10,2,69,1,2,1,1,3),_QtechWebPortalWebAuthType_Type())
qtechWebPortalWebAuthType.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechWebPortalWebAuthType.setStatus(_A)
class _QtechWebPortalUseGlbConfigFlag_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_QtechWebPortalUseGlbConfigFlag_Type.__name__=_E
_QtechWebPortalUseGlbConfigFlag_Object=MibTableColumn
qtechWebPortalUseGlbConfigFlag=_QtechWebPortalUseGlbConfigFlag_Object((1,3,6,1,4,1,27514,1,1,10,2,69,1,2,1,1,4),_QtechWebPortalUseGlbConfigFlag_Type())
qtechWebPortalUseGlbConfigFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechWebPortalUseGlbConfigFlag.setStatus(_A)
class _QtechWebPortalMetholdList_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_QtechWebPortalMetholdList_Type.__name__=_C
_QtechWebPortalMetholdList_Object=MibTableColumn
qtechWebPortalMetholdList=_QtechWebPortalMetholdList_Object((1,3,6,1,4,1,27514,1,1,10,2,69,1,2,1,1,5),_QtechWebPortalMetholdList_Type())
qtechWebPortalMetholdList.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechWebPortalMetholdList.setStatus(_A)
class _QtechWebPortalCustomizedPageName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,130))
_QtechWebPortalCustomizedPageName_Type.__name__=_C
_QtechWebPortalCustomizedPageName_Object=MibTableColumn
qtechWebPortalCustomizedPageName=_QtechWebPortalCustomizedPageName_Object((1,3,6,1,4,1,27514,1,1,10,2,69,1,2,1,1,6),_QtechWebPortalCustomizedPageName_Type())
qtechWebPortalCustomizedPageName.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechWebPortalCustomizedPageName.setStatus(_A)
class _QtechWebPortalExtWebPortalURL_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,130))
_QtechWebPortalExtWebPortalURL_Type.__name__=_C
_QtechWebPortalExtWebPortalURL_Object=MibTableColumn
qtechWebPortalExtWebPortalURL=_QtechWebPortalExtWebPortalURL_Object((1,3,6,1,4,1,27514,1,1,10,2,69,1,2,1,1,7),_QtechWebPortalExtWebPortalURL_Type())
qtechWebPortalExtWebPortalURL.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechWebPortalExtWebPortalURL.setStatus(_A)
class _QtechWebPortalCustomizedLogoName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,130))
_QtechWebPortalCustomizedLogoName_Type.__name__=_C
_QtechWebPortalCustomizedLogoName_Object=MibTableColumn
qtechWebPortalCustomizedLogoName=_QtechWebPortalCustomizedLogoName_Object((1,3,6,1,4,1,27514,1,1,10,2,69,1,2,1,1,8),_QtechWebPortalCustomizedLogoName_Type())
qtechWebPortalCustomizedLogoName.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechWebPortalCustomizedLogoName.setStatus(_A)
class _QtechWebPortalEchoManufacturerLogo_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_QtechWebPortalEchoManufacturerLogo_Type.__name__=_E
_QtechWebPortalEchoManufacturerLogo_Object=MibTableColumn
qtechWebPortalEchoManufacturerLogo=_QtechWebPortalEchoManufacturerLogo_Object((1,3,6,1,4,1,27514,1,1,10,2,69,1,2,1,1,9),_QtechWebPortalEchoManufacturerLogo_Type())
qtechWebPortalEchoManufacturerLogo.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechWebPortalEchoManufacturerLogo.setStatus(_A)
class _QtechWebPortalWelcomeMsg_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,2047))
_QtechWebPortalWelcomeMsg_Type.__name__=_G
_QtechWebPortalWelcomeMsg_Object=MibTableColumn
qtechWebPortalWelcomeMsg=_QtechWebPortalWelcomeMsg_Object((1,3,6,1,4,1,27514,1,1,10,2,69,1,2,1,1,10),_QtechWebPortalWelcomeMsg_Type())
qtechWebPortalWelcomeMsg.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechWebPortalWelcomeMsg.setStatus(_A)
class _QtechWebPortalWebPageTitle_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,130))
_QtechWebPortalWebPageTitle_Type.__name__=_C
_QtechWebPortalWebPageTitle_Object=MibTableColumn
qtechWebPortalWebPageTitle=_QtechWebPortalWebPageTitle_Object((1,3,6,1,4,1,27514,1,1,10,2,69,1,2,1,1,11),_QtechWebPortalWebPageTitle_Type())
qtechWebPortalWebPageTitle.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechWebPortalWebPageTitle.setStatus(_A)
_QtechWebPortalEntryStatus_Type=RowStatus
_QtechWebPortalEntryStatus_Object=MibTableColumn
qtechWebPortalEntryStatus=_QtechWebPortalEntryStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,69,1,2,1,1,12),_QtechWebPortalEntryStatus_Type())
qtechWebPortalEntryStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechWebPortalEntryStatus.setStatus(_A)
_QtechWebPortalMIBConformance_ObjectIdentity=ObjectIdentity
qtechWebPortalMIBConformance=_QtechWebPortalMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,69,2))
_QtechWebPortalMIBCompliances_ObjectIdentity=ObjectIdentity
qtechWebPortalMIBCompliances=_QtechWebPortalMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,69,2,1))
_QtechWebPortalMIBGroups_ObjectIdentity=ObjectIdentity
qtechWebPortalMIBGroups=_QtechWebPortalMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,69,2,2))
qtechWebPortalMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,69,2,2,1))
qtechWebPortalMIBGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_J),(_B,_K),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:qtechWebPortalMIBGroup.setStatus(_A)
qtechWebPortalMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,69,2,1,1))
qtechWebPortalMIBCompliance.setObjects((_B,_h))
if mibBuilder.loadTexts:qtechWebPortalMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qtechWebPortalMIB':qtechWebPortalMIB,'qtechWebPortalMIBObjects':qtechWebPortalMIBObjects,'qtechWebPortalGlobalMIBObjects':qtechWebPortalGlobalMIBObjects,_P:qtechWebPortalGlbWebAuthType,_Q:qtechWebPortalGlbMethodList,_R:qtechWebPortalGlbCustomizedPageName,_S:qtechWebPortalGlbExternalWebPortalURL,_T:qtechWebPortalGlbCustomizedLogoName,_U:qtechWebPortalGlbEchoManufacturerLogo,_V:qtechWebPortalGlbWelcomeMsg,_W:qtechWebPortalGlbWebPageTitle,'qtechWebPortalLocalMIBObjects':qtechWebPortalLocalMIBObjects,'qtechWebPortalAuthTable':qtechWebPortalAuthTable,'qtechWebPortalAuthEntry':qtechWebPortalAuthEntry,_J:qtechWebPortalNetMode,_K:qtechWebPortalNetID,_X:qtechWebPortalWebAuthType,_Y:qtechWebPortalUseGlbConfigFlag,_Z:qtechWebPortalMetholdList,_a:qtechWebPortalCustomizedPageName,_b:qtechWebPortalExtWebPortalURL,_c:qtechWebPortalCustomizedLogoName,_d:qtechWebPortalEchoManufacturerLogo,_e:qtechWebPortalWelcomeMsg,_f:qtechWebPortalWebPageTitle,_g:qtechWebPortalEntryStatus,'qtechWebPortalMIBConformance':qtechWebPortalMIBConformance,'qtechWebPortalMIBCompliances':qtechWebPortalMIBCompliances,'qtechWebPortalMIBCompliance':qtechWebPortalMIBCompliance,'qtechWebPortalMIBGroups':qtechWebPortalMIBGroups,_h:qtechWebPortalMIBGroup})