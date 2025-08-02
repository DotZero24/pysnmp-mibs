_J='enabled'
_I='guiElementIndex'
_H='normal'
_G='not-accessible'
_F='guiPageIndex'
_E='G6-WEB-MIB'
_D='disabled'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
g6,=mibBuilder.importSymbols('MICROSENS-G6-MIB','g6')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
management=ModuleIdentity((1,3,6,1,4,1,3181,10,6,3))
if mibBuilder.loadTexts:management.setRevisions(('2018-02-12 16:19',))
_Web_ObjectIdentity=ObjectIdentity
web=_Web_ObjectIdentity((1,3,6,1,4,1,3181,10,6,3,63))
class _WebProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_D,0),('httpUnsecure',1),('httpsSecure',2)))
_WebProtocol_Type.__name__=_C
_WebProtocol_Object=MibScalar
webProtocol=_WebProtocol_Object((1,3,6,1,4,1,3181,10,6,3,63,1),_WebProtocol_Type())
webProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:webProtocol.setStatus(_A)
class _WebWebTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WebWebTimeout_Type.__name__=_C
_WebWebTimeout_Object=MibScalar
webWebTimeout=_WebWebTimeout_Object((1,3,6,1,4,1,3181,10,6,3,63,2),_WebWebTimeout_Type())
webWebTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:webWebTimeout.setStatus(_A)
class _WebHttpPortWeb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WebHttpPortWeb_Type.__name__=_C
_WebHttpPortWeb_Object=MibScalar
webHttpPortWeb=_WebHttpPortWeb_Object((1,3,6,1,4,1,3181,10,6,3,63,3),_WebHttpPortWeb_Type())
webHttpPortWeb.setMaxAccess(_B)
if mibBuilder.loadTexts:webHttpPortWeb.setStatus(_A)
class _WebHttpsPortWeb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WebHttpsPortWeb_Type.__name__=_C
_WebHttpsPortWeb_Object=MibScalar
webHttpsPortWeb=_WebHttpsPortWeb_Object((1,3,6,1,4,1,3181,10,6,3,63,4),_WebHttpsPortWeb_Type())
webHttpsPortWeb.setMaxAccess(_B)
if mibBuilder.loadTexts:webHttpsPortWeb.setStatus(_A)
class _WebCertificateSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('intern',0),('custom',1)))
_WebCertificateSource_Type.__name__=_C
_WebCertificateSource_Object=MibScalar
webCertificateSource=_WebCertificateSource_Object((1,3,6,1,4,1,3181,10,6,3,63,5),_WebCertificateSource_Type())
webCertificateSource.setMaxAccess(_B)
if mibBuilder.loadTexts:webCertificateSource.setStatus(_A)
_WebLoginMessage_Type=DisplayString
_WebLoginMessage_Object=MibScalar
webLoginMessage=_WebLoginMessage_Object((1,3,6,1,4,1,3181,10,6,3,63,6),_WebLoginMessage_Type())
webLoginMessage.setMaxAccess(_B)
if mibBuilder.loadTexts:webLoginMessage.setStatus(_A)
_GuiPageTable_Object=MibTable
guiPageTable=_GuiPageTable_Object((1,3,6,1,4,1,3181,10,6,3,63,7))
if mibBuilder.loadTexts:guiPageTable.setStatus(_A)
_GuiPageEntry_Object=MibTableRow
guiPageEntry=_GuiPageEntry_Object((1,3,6,1,4,1,3181,10,6,3,63,7,1))
guiPageEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:guiPageEntry.setStatus(_A)
class _GuiPageIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_GuiPageIndex_Type.__name__=_C
_GuiPageIndex_Object=MibTableColumn
guiPageIndex=_GuiPageIndex_Object((1,3,6,1,4,1,3181,10,6,3,63,7,1,1),_GuiPageIndex_Type())
guiPageIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:guiPageIndex.setStatus(_A)
_GuiPageName_Type=DisplayString
_GuiPageName_Object=MibTableColumn
guiPageName=_GuiPageName_Object((1,3,6,1,4,1,3181,10,6,3,63,7,1,2),_GuiPageName_Type())
guiPageName.setMaxAccess(_B)
if mibBuilder.loadTexts:guiPageName.setStatus(_A)
class _GuiPageGuiMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_D,0),('displayOnly',1),(_H,2),('remoteOnly',3)))
_GuiPageGuiMode_Type.__name__=_C
_GuiPageGuiMode_Object=MibTableColumn
guiPageGuiMode=_GuiPageGuiMode_Object((1,3,6,1,4,1,3181,10,6,3,63,7,1,3),_GuiPageGuiMode_Type())
guiPageGuiMode.setMaxAccess(_B)
if mibBuilder.loadTexts:guiPageGuiMode.setStatus(_A)
class _GuiPageColorScheme_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('gray',0),('blue',1),('red',2),('lime',3),('yellow',4),('pink',5),('cyan',6),('green',7),('orange',8),('purple',9),('teal',10)))
_GuiPageColorScheme_Type.__name__=_C
_GuiPageColorScheme_Object=MibTableColumn
guiPageColorScheme=_GuiPageColorScheme_Object((1,3,6,1,4,1,3181,10,6,3,63,7,1,4),_GuiPageColorScheme_Type())
guiPageColorScheme.setMaxAccess(_B)
if mibBuilder.loadTexts:guiPageColorScheme.setStatus(_A)
_GuiPageLimitedToUsers_Type=DisplayString
_GuiPageLimitedToUsers_Object=MibTableColumn
guiPageLimitedToUsers=_GuiPageLimitedToUsers_Object((1,3,6,1,4,1,3181,10,6,3,63,7,1,5),_GuiPageLimitedToUsers_Type())
guiPageLimitedToUsers.setMaxAccess(_B)
if mibBuilder.loadTexts:guiPageLimitedToUsers.setStatus(_A)
_GuiPageOptions_Type=DisplayString
_GuiPageOptions_Object=MibTableColumn
guiPageOptions=_GuiPageOptions_Object((1,3,6,1,4,1,3181,10,6,3,63,7,1,6),_GuiPageOptions_Type())
guiPageOptions.setMaxAccess(_B)
if mibBuilder.loadTexts:guiPageOptions.setStatus(_A)
_GuiElementTable_Object=MibTable
guiElementTable=_GuiElementTable_Object((1,3,6,1,4,1,3181,10,6,3,63,8))
if mibBuilder.loadTexts:guiElementTable.setStatus(_A)
_GuiElementEntry_Object=MibTableRow
guiElementEntry=_GuiElementEntry_Object((1,3,6,1,4,1,3181,10,6,3,63,8,1))
guiElementEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:guiElementEntry.setStatus(_A)
class _GuiElementIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_GuiElementIndex_Type.__name__=_C
_GuiElementIndex_Object=MibTableColumn
guiElementIndex=_GuiElementIndex_Object((1,3,6,1,4,1,3181,10,6,3,63,8,1,1),_GuiElementIndex_Type())
guiElementIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:guiElementIndex.setStatus(_A)
_GuiElementName_Type=DisplayString
_GuiElementName_Object=MibTableColumn
guiElementName=_GuiElementName_Object((1,3,6,1,4,1,3181,10,6,3,63,8,1,2),_GuiElementName_Type())
guiElementName.setMaxAccess(_B)
if mibBuilder.loadTexts:guiElementName.setStatus(_A)
class _GuiElementType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(10,11,12,13,14,15,30,31,32,33,34,50,51,52,53,54,55)));namedValues=NamedValues(*(('label',10),('image',11),('hyperLink',12),('space',13),('line',14),('frame',15),('button',30),('selectBox',31),('slider',32),('radioButton',33),('toggle',34),('textBox',50),('barGraph',51),('gauge',52),('symbol',53),('diagram',54),('input',55)))
_GuiElementType_Type.__name__=_C
_GuiElementType_Object=MibTableColumn
guiElementType=_GuiElementType_Object((1,3,6,1,4,1,3181,10,6,3,63,8,1,3),_GuiElementType_Type())
guiElementType.setMaxAccess(_B)
if mibBuilder.loadTexts:guiElementType.setStatus(_A)
_GuiElementPage_Type=DisplayString
_GuiElementPage_Object=MibTableColumn
guiElementPage=_GuiElementPage_Object((1,3,6,1,4,1,3181,10,6,3,63,8,1,4),_GuiElementPage_Type())
guiElementPage.setMaxAccess(_B)
if mibBuilder.loadTexts:guiElementPage.setStatus(_A)
class _GuiElementVisibility_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_H,0),('hidden',1),(_D,2)))
_GuiElementVisibility_Type.__name__=_C
_GuiElementVisibility_Object=MibTableColumn
guiElementVisibility=_GuiElementVisibility_Object((1,3,6,1,4,1,3181,10,6,3,63,8,1,5),_GuiElementVisibility_Type())
guiElementVisibility.setMaxAccess(_B)
if mibBuilder.loadTexts:guiElementVisibility.setStatus(_A)
class _GuiElementAutoSave_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_J,1)))
_GuiElementAutoSave_Type.__name__=_C
_GuiElementAutoSave_Object=MibTableColumn
guiElementAutoSave=_GuiElementAutoSave_Object((1,3,6,1,4,1,3181,10,6,3,63,8,1,6),_GuiElementAutoSave_Type())
guiElementAutoSave.setMaxAccess(_B)
if mibBuilder.loadTexts:guiElementAutoSave.setStatus(_A)
class _GuiElementRemoteAccessible_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_J,1)))
_GuiElementRemoteAccessible_Type.__name__=_C
_GuiElementRemoteAccessible_Object=MibTableColumn
guiElementRemoteAccessible=_GuiElementRemoteAccessible_Object((1,3,6,1,4,1,3181,10,6,3,63,8,1,7),_GuiElementRemoteAccessible_Type())
guiElementRemoteAccessible.setMaxAccess(_B)
if mibBuilder.loadTexts:guiElementRemoteAccessible.setStatus(_A)
_GuiElementSensorAttribute_Type=DisplayString
_GuiElementSensorAttribute_Object=MibTableColumn
guiElementSensorAttribute=_GuiElementSensorAttribute_Object((1,3,6,1,4,1,3181,10,6,3,63,8,1,8),_GuiElementSensorAttribute_Type())
guiElementSensorAttribute.setMaxAccess(_B)
if mibBuilder.loadTexts:guiElementSensorAttribute.setStatus(_A)
_GuiElementScriptName_Type=DisplayString
_GuiElementScriptName_Object=MibTableColumn
guiElementScriptName=_GuiElementScriptName_Object((1,3,6,1,4,1,3181,10,6,3,63,8,1,9),_GuiElementScriptName_Type())
guiElementScriptName.setMaxAccess(_B)
if mibBuilder.loadTexts:guiElementScriptName.setStatus(_A)
_GuiElementWatchedElement_Type=DisplayString
_GuiElementWatchedElement_Object=MibTableColumn
guiElementWatchedElement=_GuiElementWatchedElement_Object((1,3,6,1,4,1,3181,10,6,3,63,8,1,10),_GuiElementWatchedElement_Type())
guiElementWatchedElement.setMaxAccess(_B)
if mibBuilder.loadTexts:guiElementWatchedElement.setStatus(_A)
_GuiElementOrder_Type=Unsigned32
_GuiElementOrder_Object=MibTableColumn
guiElementOrder=_GuiElementOrder_Object((1,3,6,1,4,1,3181,10,6,3,63,8,1,11),_GuiElementOrder_Type())
guiElementOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:guiElementOrder.setStatus(_A)
_GuiElementHeight_Type=DisplayString
_GuiElementHeight_Object=MibTableColumn
guiElementHeight=_GuiElementHeight_Object((1,3,6,1,4,1,3181,10,6,3,63,8,1,12),_GuiElementHeight_Type())
guiElementHeight.setMaxAccess(_B)
if mibBuilder.loadTexts:guiElementHeight.setStatus(_A)
_GuiElementWidth_Type=DisplayString
_GuiElementWidth_Object=MibTableColumn
guiElementWidth=_GuiElementWidth_Object((1,3,6,1,4,1,3181,10,6,3,63,8,1,13),_GuiElementWidth_Type())
guiElementWidth.setMaxAccess(_B)
if mibBuilder.loadTexts:guiElementWidth.setStatus(_A)
_GuiElementTopMargin_Type=DisplayString
_GuiElementTopMargin_Object=MibTableColumn
guiElementTopMargin=_GuiElementTopMargin_Object((1,3,6,1,4,1,3181,10,6,3,63,8,1,14),_GuiElementTopMargin_Type())
guiElementTopMargin.setMaxAccess(_B)
if mibBuilder.loadTexts:guiElementTopMargin.setStatus(_A)
_GuiElementLeftMargin_Type=DisplayString
_GuiElementLeftMargin_Object=MibTableColumn
guiElementLeftMargin=_GuiElementLeftMargin_Object((1,3,6,1,4,1,3181,10,6,3,63,8,1,15),_GuiElementLeftMargin_Type())
guiElementLeftMargin.setMaxAccess(_B)
if mibBuilder.loadTexts:guiElementLeftMargin.setStatus(_A)
_GuiElementHeader_Type=DisplayString
_GuiElementHeader_Object=MibTableColumn
guiElementHeader=_GuiElementHeader_Object((1,3,6,1,4,1,3181,10,6,3,63,8,1,16),_GuiElementHeader_Type())
guiElementHeader.setMaxAccess(_B)
if mibBuilder.loadTexts:guiElementHeader.setStatus(_A)
_GuiElementText_Type=DisplayString
_GuiElementText_Object=MibTableColumn
guiElementText=_GuiElementText_Object((1,3,6,1,4,1,3181,10,6,3,63,8,1,17),_GuiElementText_Type())
guiElementText.setMaxAccess(_B)
if mibBuilder.loadTexts:guiElementText.setStatus(_A)
_GuiElementValue_Type=DisplayString
_GuiElementValue_Object=MibTableColumn
guiElementValue=_GuiElementValue_Object((1,3,6,1,4,1,3181,10,6,3,63,8,1,18),_GuiElementValue_Type())
guiElementValue.setMaxAccess(_B)
if mibBuilder.loadTexts:guiElementValue.setStatus(_A)
_GuiElementStartValue_Type=DisplayString
_GuiElementStartValue_Object=MibTableColumn
guiElementStartValue=_GuiElementStartValue_Object((1,3,6,1,4,1,3181,10,6,3,63,8,1,19),_GuiElementStartValue_Type())
guiElementStartValue.setMaxAccess(_B)
if mibBuilder.loadTexts:guiElementStartValue.setStatus(_A)
_GuiElementImage_Type=DisplayString
_GuiElementImage_Object=MibTableColumn
guiElementImage=_GuiElementImage_Object((1,3,6,1,4,1,3181,10,6,3,63,8,1,20),_GuiElementImage_Type())
guiElementImage.setMaxAccess(_B)
if mibBuilder.loadTexts:guiElementImage.setStatus(_A)
_GuiElementOptions_Type=DisplayString
_GuiElementOptions_Object=MibTableColumn
guiElementOptions=_GuiElementOptions_Object((1,3,6,1,4,1,3181,10,6,3,63,8,1,21),_GuiElementOptions_Type())
guiElementOptions.setMaxAccess(_B)
if mibBuilder.loadTexts:guiElementOptions.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'management':management,'web':web,'webProtocol':webProtocol,'webWebTimeout':webWebTimeout,'webHttpPortWeb':webHttpPortWeb,'webHttpsPortWeb':webHttpsPortWeb,'webCertificateSource':webCertificateSource,'webLoginMessage':webLoginMessage,'guiPageTable':guiPageTable,'guiPageEntry':guiPageEntry,_F:guiPageIndex,'guiPageName':guiPageName,'guiPageGuiMode':guiPageGuiMode,'guiPageColorScheme':guiPageColorScheme,'guiPageLimitedToUsers':guiPageLimitedToUsers,'guiPageOptions':guiPageOptions,'guiElementTable':guiElementTable,'guiElementEntry':guiElementEntry,_I:guiElementIndex,'guiElementName':guiElementName,'guiElementType':guiElementType,'guiElementPage':guiElementPage,'guiElementVisibility':guiElementVisibility,'guiElementAutoSave':guiElementAutoSave,'guiElementRemoteAccessible':guiElementRemoteAccessible,'guiElementSensorAttribute':guiElementSensorAttribute,'guiElementScriptName':guiElementScriptName,'guiElementWatchedElement':guiElementWatchedElement,'guiElementOrder':guiElementOrder,'guiElementHeight':guiElementHeight,'guiElementWidth':guiElementWidth,'guiElementTopMargin':guiElementTopMargin,'guiElementLeftMargin':guiElementLeftMargin,'guiElementHeader':guiElementHeader,'guiElementText':guiElementText,'guiElementValue':guiElementValue,'guiElementStartValue':guiElementStartValue,'guiElementImage':guiElementImage,'guiElementOptions':guiElementOptions})