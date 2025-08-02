_I='000000000000'
_H='oaSwMacVid'
_G='oaSwMacAddr'
_F='MacAddress'
_E='OASWITCH-MIB'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class MacAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_Oaccess_ObjectIdentity=ObjectIdentity
oaccess=_Oaccess_ObjectIdentity((1,3,6,1,4,1,6926))
_OaManagement_ObjectIdentity=ObjectIdentity
oaManagement=_OaManagement_ObjectIdentity((1,3,6,1,4,1,6926,1))
_OaSwitch_ObjectIdentity=ObjectIdentity
oaSwitch=_OaSwitch_ObjectIdentity((1,3,6,1,4,1,6926,1,5))
_OaSwitchMac_ObjectIdentity=ObjectIdentity
oaSwitchMac=_OaSwitchMac_ObjectIdentity((1,3,6,1,4,1,6926,1,5,1))
_OaSwitchMacInfo_ObjectIdentity=ObjectIdentity
oaSwitchMacInfo=_OaSwitchMacInfo_ObjectIdentity((1,3,6,1,4,1,6926,1,5,1,1))
_OaSwitchMacInfoNumber_Type=Integer32
_OaSwitchMacInfoNumber_Object=MibScalar
oaSwitchMacInfoNumber=_OaSwitchMacInfoNumber_Object((1,3,6,1,4,1,6926,1,5,1,1,1),_OaSwitchMacInfoNumber_Type())
oaSwitchMacInfoNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:oaSwitchMacInfoNumber.setStatus(_A)
_OaSwitchMacInfoMaxNumbr_Type=Integer32
_OaSwitchMacInfoMaxNumbr_Object=MibScalar
oaSwitchMacInfoMaxNumbr=_OaSwitchMacInfoMaxNumbr_Object((1,3,6,1,4,1,6926,1,5,1,1,2),_OaSwitchMacInfoMaxNumbr_Type())
oaSwitchMacInfoMaxNumbr.setMaxAccess(_D)
if mibBuilder.loadTexts:oaSwitchMacInfoMaxNumbr.setStatus(_A)
class _OaSwitchMacInfoClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('none',1),('clear',2)))
_OaSwitchMacInfoClear_Type.__name__=_C
_OaSwitchMacInfoClear_Object=MibScalar
oaSwitchMacInfoClear=_OaSwitchMacInfoClear_Object((1,3,6,1,4,1,6926,1,5,1,1,5),_OaSwitchMacInfoClear_Type())
oaSwitchMacInfoClear.setMaxAccess(_B)
if mibBuilder.loadTexts:oaSwitchMacInfoClear.setStatus(_A)
_OaSwMacTable_Object=MibTable
oaSwMacTable=_OaSwMacTable_Object((1,3,6,1,4,1,6926,1,5,1,2))
if mibBuilder.loadTexts:oaSwMacTable.setStatus(_A)
_OaSwMacEntry_Object=MibTableRow
oaSwMacEntry=_OaSwMacEntry_Object((1,3,6,1,4,1,6926,1,5,1,2,1))
oaSwMacEntry.setIndexNames((0,_E,_G),(0,_E,_H))
if mibBuilder.loadTexts:oaSwMacEntry.setStatus(_A)
_OaSwMacAddr_Type=MacAddress
_OaSwMacAddr_Object=MibTableColumn
oaSwMacAddr=_OaSwMacAddr_Object((1,3,6,1,4,1,6926,1,5,1,2,1,1),_OaSwMacAddr_Type())
oaSwMacAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:oaSwMacAddr.setStatus(_A)
_OaSwMacVid_Type=Integer32
_OaSwMacVid_Object=MibTableColumn
oaSwMacVid=_OaSwMacVid_Object((1,3,6,1,4,1,6926,1,5,1,2,1,2),_OaSwMacVid_Type())
oaSwMacVid.setMaxAccess(_D)
if mibBuilder.loadTexts:oaSwMacVid.setStatus(_A)
_OaSwMacVidx_Type=Integer32
_OaSwMacVidx_Object=MibTableColumn
oaSwMacVidx=_OaSwMacVidx_Object((1,3,6,1,4,1,6926,1,5,1,2,1,6),_OaSwMacVidx_Type())
oaSwMacVidx.setMaxAccess(_B)
if mibBuilder.loadTexts:oaSwMacVidx.setStatus(_A)
_OaSwMacGetViewIndex_Type=Integer32
_OaSwMacGetViewIndex_Object=MibTableColumn
oaSwMacGetViewIndex=_OaSwMacGetViewIndex_Object((1,3,6,1,4,1,6926,1,5,1,2,1,8),_OaSwMacGetViewIndex_Type())
oaSwMacGetViewIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:oaSwMacGetViewIndex.setStatus(_A)
class _OaSwMacPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_OaSwMacPort_Type.__name__=_C
_OaSwMacPort_Object=MibTableColumn
oaSwMacPort=_OaSwMacPort_Object((1,3,6,1,4,1,6926,1,5,1,2,1,9),_OaSwMacPort_Type())
oaSwMacPort.setMaxAccess(_B)
if mibBuilder.loadTexts:oaSwMacPort.setStatus(_A)
class _OaSwMacMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),('dynamic',2),('static',3)))
_OaSwMacMode_Type.__name__=_C
_OaSwMacMode_Object=MibTableColumn
oaSwMacMode=_OaSwMacMode_Object((1,3,6,1,4,1,6926,1,5,1,2,1,20),_OaSwMacMode_Type())
oaSwMacMode.setMaxAccess(_B)
if mibBuilder.loadTexts:oaSwMacMode.setStatus(_A)
class _OaSwMacTagged_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('no',0),('yes',1)))
_OaSwMacTagged_Type.__name__=_C
_OaSwMacTagged_Object=MibTableColumn
oaSwMacTagged=_OaSwMacTagged_Object((1,3,6,1,4,1,6926,1,5,1,2,1,21),_OaSwMacTagged_Type())
oaSwMacTagged.setMaxAccess(_B)
if mibBuilder.loadTexts:oaSwMacTagged.setStatus(_A)
_OaSwMacPriority_Type=Integer32
_OaSwMacPriority_Object=MibTableColumn
oaSwMacPriority=_OaSwMacPriority_Object((1,3,6,1,4,1,6926,1,5,1,2,1,22),_OaSwMacPriority_Type())
oaSwMacPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:oaSwMacPriority.setStatus(_A)
_OaSwMacFlags_Type=Integer32
_OaSwMacFlags_Object=MibTableColumn
oaSwMacFlags=_OaSwMacFlags_Object((1,3,6,1,4,1,6926,1,5,1,2,1,23),_OaSwMacFlags_Type())
oaSwMacFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:oaSwMacFlags.setStatus(_A)
class _OaSwMacStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),('invalid',2)))
_OaSwMacStatus_Type.__name__=_C
_OaSwMacStatus_Object=MibTableColumn
oaSwMacStatus=_OaSwMacStatus_Object((1,3,6,1,4,1,6926,1,5,1,2,1,30),_OaSwMacStatus_Type())
oaSwMacStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oaSwMacStatus.setStatus(_A)
_OaSysFrmGen_ObjectIdentity=ObjectIdentity
oaSysFrmGen=_OaSysFrmGen_ObjectIdentity((1,3,6,1,4,1,6926,1,5,3))
class _OaSysFrmGenSession_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('idleFG',1),('runFG',2)))
_OaSysFrmGenSession_Type.__name__=_C
_OaSysFrmGenSession_Object=MibScalar
oaSysFrmGenSession=_OaSysFrmGenSession_Object((1,3,6,1,4,1,6926,1,5,3,1),_OaSysFrmGenSession_Type())
oaSysFrmGenSession.setMaxAccess(_B)
if mibBuilder.loadTexts:oaSysFrmGenSession.setStatus(_A)
class _OaSysFrmGenDa_Type(MacAddress):defaultHexValue=_I
_OaSysFrmGenDa_Type.__name__=_F
_OaSysFrmGenDa_Object=MibScalar
oaSysFrmGenDa=_OaSysFrmGenDa_Object((1,3,6,1,4,1,6926,1,5,3,2),_OaSysFrmGenDa_Type())
oaSysFrmGenDa.setMaxAccess(_B)
if mibBuilder.loadTexts:oaSysFrmGenDa.setStatus(_A)
class _OaSysFrmGenSa_Type(MacAddress):defaultHexValue=_I
_OaSysFrmGenSa_Type.__name__=_F
_OaSysFrmGenSa_Object=MibScalar
oaSysFrmGenSa=_OaSysFrmGenSa_Object((1,3,6,1,4,1,6926,1,5,3,3),_OaSysFrmGenSa_Type())
oaSysFrmGenSa.setMaxAccess(_B)
if mibBuilder.loadTexts:oaSysFrmGenSa.setStatus(_A)
_OaSysFrmGenPktFill_Type=Integer32
_OaSysFrmGenPktFill_Object=MibScalar
oaSysFrmGenPktFill=_OaSysFrmGenPktFill_Object((1,3,6,1,4,1,6926,1,5,3,4),_OaSysFrmGenPktFill_Type())
oaSysFrmGenPktFill.setMaxAccess(_B)
if mibBuilder.loadTexts:oaSysFrmGenPktFill.setStatus(_A)
_OaSysFrmGenPktRate_Type=Integer32
_OaSysFrmGenPktRate_Object=MibScalar
oaSysFrmGenPktRate=_OaSysFrmGenPktRate_Object((1,3,6,1,4,1,6926,1,5,3,5),_OaSysFrmGenPktRate_Type())
oaSysFrmGenPktRate.setMaxAccess(_B)
if mibBuilder.loadTexts:oaSysFrmGenPktRate.setStatus(_A)
_OaSysFrmGenDestMap_Type=OctetString
_OaSysFrmGenDestMap_Object=MibScalar
oaSysFrmGenDestMap=_OaSysFrmGenDestMap_Object((1,3,6,1,4,1,6926,1,5,3,6),_OaSysFrmGenDestMap_Type())
oaSysFrmGenDestMap.setMaxAccess(_B)
if mibBuilder.loadTexts:oaSysFrmGenDestMap.setStatus(_A)
_OaSysFrmGenPktNum_Type=Counter32
_OaSysFrmGenPktNum_Object=MibScalar
oaSysFrmGenPktNum=_OaSysFrmGenPktNum_Object((1,3,6,1,4,1,6926,1,5,3,7),_OaSysFrmGenPktNum_Type())
oaSysFrmGenPktNum.setMaxAccess(_B)
if mibBuilder.loadTexts:oaSysFrmGenPktNum.setStatus(_A)
_OaSysFrmGenPktLen_Type=Integer32
_OaSysFrmGenPktLen_Object=MibScalar
oaSysFrmGenPktLen=_OaSysFrmGenPktLen_Object((1,3,6,1,4,1,6926,1,5,3,8),_OaSysFrmGenPktLen_Type())
oaSysFrmGenPktLen.setMaxAccess(_B)
if mibBuilder.loadTexts:oaSysFrmGenPktLen.setStatus(_A)
_OaSysFrmGenXmtPktNum_Type=Counter32
_OaSysFrmGenXmtPktNum_Object=MibScalar
oaSysFrmGenXmtPktNum=_OaSysFrmGenXmtPktNum_Object((1,3,6,1,4,1,6926,1,5,3,9),_OaSysFrmGenXmtPktNum_Type())
oaSysFrmGenXmtPktNum.setMaxAccess(_D)
if mibBuilder.loadTexts:oaSysFrmGenXmtPktNum.setStatus(_A)
class _OaSysFrmGenPriority_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_OaSysFrmGenPriority_Type.__name__=_C
_OaSysFrmGenPriority_Object=MibScalar
oaSysFrmGenPriority=_OaSysFrmGenPriority_Object((1,3,6,1,4,1,6926,1,5,3,10),_OaSysFrmGenPriority_Type())
oaSysFrmGenPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:oaSysFrmGenPriority.setStatus(_A)
class _OaSysFrmGenVlanId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_OaSysFrmGenVlanId_Type.__name__=_C
_OaSysFrmGenVlanId_Object=MibScalar
oaSysFrmGenVlanId=_OaSysFrmGenVlanId_Object((1,3,6,1,4,1,6926,1,5,3,11),_OaSysFrmGenVlanId_Type())
oaSysFrmGenVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:oaSysFrmGenVlanId.setStatus(_A)
mibBuilder.exportSymbols(_E,**{_F:MacAddress,'oaccess':oaccess,'oaManagement':oaManagement,'oaSwitch':oaSwitch,'oaSwitchMac':oaSwitchMac,'oaSwitchMacInfo':oaSwitchMacInfo,'oaSwitchMacInfoNumber':oaSwitchMacInfoNumber,'oaSwitchMacInfoMaxNumbr':oaSwitchMacInfoMaxNumbr,'oaSwitchMacInfoClear':oaSwitchMacInfoClear,'oaSwMacTable':oaSwMacTable,'oaSwMacEntry':oaSwMacEntry,_G:oaSwMacAddr,_H:oaSwMacVid,'oaSwMacVidx':oaSwMacVidx,'oaSwMacGetViewIndex':oaSwMacGetViewIndex,'oaSwMacPort':oaSwMacPort,'oaSwMacMode':oaSwMacMode,'oaSwMacTagged':oaSwMacTagged,'oaSwMacPriority':oaSwMacPriority,'oaSwMacFlags':oaSwMacFlags,'oaSwMacStatus':oaSwMacStatus,'oaSysFrmGen':oaSysFrmGen,'oaSysFrmGenSession':oaSysFrmGenSession,'oaSysFrmGenDa':oaSysFrmGenDa,'oaSysFrmGenSa':oaSysFrmGenSa,'oaSysFrmGenPktFill':oaSysFrmGenPktFill,'oaSysFrmGenPktRate':oaSysFrmGenPktRate,'oaSysFrmGenDestMap':oaSysFrmGenDestMap,'oaSysFrmGenPktNum':oaSysFrmGenPktNum,'oaSysFrmGenPktLen':oaSysFrmGenPktLen,'oaSysFrmGenXmtPktNum':oaSysFrmGenXmtPktNum,'oaSysFrmGenPriority':oaSysFrmGenPriority,'oaSysFrmGenVlanId':oaSysFrmGenVlanId})