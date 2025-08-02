_a='Integer32'
_Z='mandatory'
_Y='read-only'
_X='altDetectorID'
_W='altEventType'
_V='altCommonEventID'
_U='altAuxData'
_T='altHostMTM'
_S='altFailingFRUs'
_R='altTest'
_Q='altServiceable'
_P='altEventID'
_O='altHostBladeBay'
_N='altHostLowestUpos'
_M='altHostRackID'
_L='altHostRoomID'
_K='altHostLocation'
_J='altHostContact'
_I='altMsgText'
_H='altPriority'
_G='altMsgIDPrefix'
_F='altMsgID'
_E='altSysSern'
_D='altSysUuid'
_C='altSpTxtId'
_B='altDateTime'
_A='IMMALERT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_a,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso','mib-2')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Ibm_ObjectIdentity=ObjectIdentity
ibm=_Ibm_ObjectIdentity((1,3,6,1,4,1,2))
_IbmProd_ObjectIdentity=ObjectIdentity
ibmProd=_IbmProd_ObjectIdentity((1,3,6,1,4,1,2,6))
_SupportProcessor_ObjectIdentity=ObjectIdentity
supportProcessor=_SupportProcessor_ObjectIdentity((1,3,6,1,4,1,2,6,158))
_ImmalertMIB_ObjectIdentity=ObjectIdentity
immalertMIB=_ImmalertMIB_ObjectIdentity((1,3,6,1,4,1,2,6,158,5))
_Immtrapg_ObjectIdentity=ObjectIdentity
immtrapg=_Immtrapg_ObjectIdentity((1,3,6,1,4,1,2,6,158,5,1))
_AltDateTime_Type=DisplayString
_AltDateTime_Object=MibScalar
altDateTime=_AltDateTime_Object((1,3,6,1,4,1,2,6,158,5,1,1),_AltDateTime_Type())
altDateTime.setMaxAccess(_Y)
if mibBuilder.loadTexts:altDateTime.setStatus(_Z)
_AltSpTxtId_Type=DisplayString
_AltSpTxtId_Object=MibScalar
altSpTxtId=_AltSpTxtId_Object((1,3,6,1,4,1,2,6,158,5,1,3),_AltSpTxtId_Type())
altSpTxtId.setMaxAccess(_Y)
if mibBuilder.loadTexts:altSpTxtId.setStatus(_Z)
_AltSysUuid_Type=DisplayString
_AltSysUuid_Object=MibScalar
altSysUuid=_AltSysUuid_Object((1,3,6,1,4,1,2,6,158,5,1,5),_AltSysUuid_Type())
altSysUuid.setMaxAccess(_Y)
if mibBuilder.loadTexts:altSysUuid.setStatus(_Z)
_AltSysSern_Type=DisplayString
_AltSysSern_Object=MibScalar
altSysSern=_AltSysSern_Object((1,3,6,1,4,1,2,6,158,5,1,6),_AltSysSern_Type())
altSysSern.setMaxAccess(_Y)
if mibBuilder.loadTexts:altSysSern.setStatus(_Z)
class _AltPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AltPriority_Type.__name__=_a
_AltPriority_Object=MibScalar
altPriority=_AltPriority_Object((1,3,6,1,4,1,2,6,158,5,1,8),_AltPriority_Type())
altPriority.setMaxAccess(_Y)
if mibBuilder.loadTexts:altPriority.setStatus(_Z)
_AltMsgText_Type=DisplayString
_AltMsgText_Object=MibScalar
altMsgText=_AltMsgText_Object((1,3,6,1,4,1,2,6,158,5,1,9),_AltMsgText_Type())
altMsgText.setMaxAccess(_Y)
if mibBuilder.loadTexts:altMsgText.setStatus(_Z)
_AltMsgID_Type=Integer32
_AltMsgID_Object=MibScalar
altMsgID=_AltMsgID_Object((1,3,6,1,4,1,2,6,158,5,1,10),_AltMsgID_Type())
altMsgID.setMaxAccess(_Y)
if mibBuilder.loadTexts:altMsgID.setStatus(_Z)
_AltMsgIDPrefix_Type=DisplayString
_AltMsgIDPrefix_Object=MibScalar
altMsgIDPrefix=_AltMsgIDPrefix_Object((1,3,6,1,4,1,2,6,158,5,1,11),_AltMsgIDPrefix_Type())
altMsgIDPrefix.setMaxAccess(_Y)
if mibBuilder.loadTexts:altMsgIDPrefix.setStatus(_Z)
_AltHostContact_Type=DisplayString
_AltHostContact_Object=MibScalar
altHostContact=_AltHostContact_Object((1,3,6,1,4,1,2,6,158,5,1,12),_AltHostContact_Type())
altHostContact.setMaxAccess(_Y)
if mibBuilder.loadTexts:altHostContact.setStatus(_Z)
_AltHostLocation_Type=DisplayString
_AltHostLocation_Object=MibScalar
altHostLocation=_AltHostLocation_Object((1,3,6,1,4,1,2,6,158,5,1,13),_AltHostLocation_Type())
altHostLocation.setMaxAccess(_Y)
if mibBuilder.loadTexts:altHostLocation.setStatus(_Z)
_AltHostRoomID_Type=DisplayString
_AltHostRoomID_Object=MibScalar
altHostRoomID=_AltHostRoomID_Object((1,3,6,1,4,1,2,6,158,5,1,14),_AltHostRoomID_Type())
altHostRoomID.setMaxAccess(_Y)
if mibBuilder.loadTexts:altHostRoomID.setStatus(_Z)
_AltHostRackID_Type=DisplayString
_AltHostRackID_Object=MibScalar
altHostRackID=_AltHostRackID_Object((1,3,6,1,4,1,2,6,158,5,1,15),_AltHostRackID_Type())
altHostRackID.setMaxAccess(_Y)
if mibBuilder.loadTexts:altHostRackID.setStatus(_Z)
_AltHostLowestUpos_Type=DisplayString
_AltHostLowestUpos_Object=MibScalar
altHostLowestUpos=_AltHostLowestUpos_Object((1,3,6,1,4,1,2,6,158,5,1,16),_AltHostLowestUpos_Type())
altHostLowestUpos.setMaxAccess(_Y)
if mibBuilder.loadTexts:altHostLowestUpos.setStatus(_Z)
_AltHostBladeBay_Type=DisplayString
_AltHostBladeBay_Object=MibScalar
altHostBladeBay=_AltHostBladeBay_Object((1,3,6,1,4,1,2,6,158,5,1,17),_AltHostBladeBay_Type())
altHostBladeBay.setMaxAccess(_Y)
if mibBuilder.loadTexts:altHostBladeBay.setStatus(_Z)
_AltEventID_Type=DisplayString
_AltEventID_Object=MibScalar
altEventID=_AltEventID_Object((1,3,6,1,4,1,2,6,158,5,1,18),_AltEventID_Type())
altEventID.setMaxAccess(_Y)
if mibBuilder.loadTexts:altEventID.setStatus(_Z)
class _AltServiceable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('notServiceable',0),('serviceableByIBM',1),('serviceableByCustomer',2)))
_AltServiceable_Type.__name__=_a
_AltServiceable_Object=MibScalar
altServiceable=_AltServiceable_Object((1,3,6,1,4,1,2,6,158,5,1,19),_AltServiceable_Type())
altServiceable.setMaxAccess(_Y)
if mibBuilder.loadTexts:altServiceable.setStatus(_Z)
class _AltTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('false',0),('true',1)))
_AltTest_Type.__name__=_a
_AltTest_Object=MibScalar
altTest=_AltTest_Object((1,3,6,1,4,1,2,6,158,5,1,20),_AltTest_Type())
altTest.setMaxAccess(_Y)
if mibBuilder.loadTexts:altTest.setStatus(_Z)
_AltFailingFRUs_Type=DisplayString
_AltFailingFRUs_Object=MibScalar
altFailingFRUs=_AltFailingFRUs_Object((1,3,6,1,4,1,2,6,158,5,1,21),_AltFailingFRUs_Type())
altFailingFRUs.setMaxAccess(_Y)
if mibBuilder.loadTexts:altFailingFRUs.setStatus(_Z)
_AltHostMTM_Type=DisplayString
_AltHostMTM_Object=MibScalar
altHostMTM=_AltHostMTM_Object((1,3,6,1,4,1,2,6,158,5,1,22),_AltHostMTM_Type())
altHostMTM.setMaxAccess(_Y)
if mibBuilder.loadTexts:altHostMTM.setStatus(_Z)
_AltAuxData_Type=DisplayString
_AltAuxData_Object=MibScalar
altAuxData=_AltAuxData_Object((1,3,6,1,4,1,2,6,158,5,1,23),_AltAuxData_Type())
altAuxData.setMaxAccess(_Y)
if mibBuilder.loadTexts:altAuxData.setStatus(_Z)
_AltCommonEventID_Type=DisplayString
_AltCommonEventID_Object=MibScalar
altCommonEventID=_AltCommonEventID_Object((1,3,6,1,4,1,2,6,158,5,1,24),_AltCommonEventID_Type())
altCommonEventID.setMaxAccess(_Y)
if mibBuilder.loadTexts:altCommonEventID.setStatus(_Z)
class _AltEventType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AltEventType_Type.__name__=_a
_AltEventType_Object=MibScalar
altEventType=_AltEventType_Object((1,3,6,1,4,1,2,6,158,5,1,25),_AltEventType_Type())
altEventType.setMaxAccess(_Y)
if mibBuilder.loadTexts:altEventType.setStatus(_Z)
_AltDetectorID_Type=DisplayString
_AltDetectorID_Object=MibScalar
altDetectorID=_AltDetectorID_Object((1,3,6,1,4,1,2,6,158,5,1,26),_AltDetectorID_Type())
altDetectorID.setMaxAccess(_Y)
if mibBuilder.loadTexts:altDetectorID.setStatus(_Z)
ibmSpTrapTempC=NotificationType((1,3,6,1,4,1,2,6,158,5,0,0))
ibmSpTrapTempC.setObjects(*((_A,_B),(_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:ibmSpTrapTempC.setStatus('')
ibmSpTrapVoltC=NotificationType((1,3,6,1,4,1,2,6,158,5,0,1))
ibmSpTrapVoltC.setObjects(*((_A,_B),(_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:ibmSpTrapVoltC.setStatus('')
ibmSpTrapPowerC=NotificationType((1,3,6,1,4,1,2,6,158,5,0,4))
ibmSpTrapPowerC.setObjects(*((_A,_B),(_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:ibmSpTrapPowerC.setStatus('')
ibmSpTrapHdC=NotificationType((1,3,6,1,4,1,2,6,158,5,0,5))
ibmSpTrapHdC.setObjects(*((_A,_B),(_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:ibmSpTrapHdC.setStatus('')
ibmSpTrapRdpsC=NotificationType((1,3,6,1,4,1,2,6,158,5,0,9))
ibmSpTrapRdpsC.setObjects(*((_A,_B),(_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:ibmSpTrapRdpsC.setStatus('')
ibmSpTrapRdpsN=NotificationType((1,3,6,1,4,1,2,6,158,5,0,10))
ibmSpTrapRdpsN.setObjects(*((_A,_B),(_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:ibmSpTrapRdpsN.setStatus('')
ibmSpTrapFanC=NotificationType((1,3,6,1,4,1,2,6,158,5,0,11))
ibmSpTrapFanC.setObjects(*((_A,_B),(_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:ibmSpTrapFanC.setStatus('')
ibmSpTrapTempN=NotificationType((1,3,6,1,4,1,2,6,158,5,0,12))
ibmSpTrapTempN.setObjects(*((_A,_B),(_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:ibmSpTrapTempN.setStatus('')
ibmSpTrapVoltN=NotificationType((1,3,6,1,4,1,2,6,158,5,0,13))
ibmSpTrapVoltN.setObjects(*((_A,_B),(_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:ibmSpTrapVoltN.setStatus('')
ibmSpTrapOsToS=NotificationType((1,3,6,1,4,1,2,6,158,5,0,21))
ibmSpTrapOsToS.setObjects(*((_A,_B),(_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:ibmSpTrapOsToS.setStatus('')
ibmSpTrapAppS=NotificationType((1,3,6,1,4,1,2,6,158,5,0,22))
ibmSpTrapAppS.setObjects(*((_A,_B),(_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:ibmSpTrapAppS.setStatus('')
ibmSpTrapPoffS=NotificationType((1,3,6,1,4,1,2,6,158,5,0,23))
ibmSpTrapPoffS.setObjects(*((_A,_B),(_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:ibmSpTrapPoffS.setStatus('')
ibmSpTrapPonS=NotificationType((1,3,6,1,4,1,2,6,158,5,0,24))
ibmSpTrapPonS.setObjects(*((_A,_B),(_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:ibmSpTrapPonS.setStatus('')
ibmSpTrapBootS=NotificationType((1,3,6,1,4,1,2,6,158,5,0,25))
ibmSpTrapBootS.setObjects(*((_A,_B),(_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:ibmSpTrapBootS.setStatus('')
ibmSpTrapLdrToS=NotificationType((1,3,6,1,4,1,2,6,158,5,0,26))
ibmSpTrapLdrToS.setObjects(*((_A,_B),(_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:ibmSpTrapLdrToS.setStatus('')
ibmSpTrapPFAS=NotificationType((1,3,6,1,4,1,2,6,158,5,0,27))
ibmSpTrapPFAS.setObjects(*((_A,_B),(_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:ibmSpTrapPFAS.setStatus('')
ibmSpTrapRLogin=NotificationType((1,3,6,1,4,1,2,6,158,5,0,30))
ibmSpTrapRLogin.setObjects(*((_A,_B),(_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:ibmSpTrapRLogin.setStatus('')
ibmSpTrapSysLogS=NotificationType((1,3,6,1,4,1,2,6,158,5,0,35))
ibmSpTrapSysLogS.setObjects(*((_A,_B),(_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:ibmSpTrapSysLogS.setStatus('')
ibmSpTrapIhcC=NotificationType((1,3,6,1,4,1,2,6,158,5,0,36))
ibmSpTrapIhcC.setObjects(*((_A,_B),(_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:ibmSpTrapIhcC.setStatus('')
ibmSpTrapNwChangeS=NotificationType((1,3,6,1,4,1,2,6,158,5,0,37))
ibmSpTrapNwChangeS.setObjects(*((_A,_B),(_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:ibmSpTrapNwChangeS.setStatus('')
ibmSpTrapCPUC=NotificationType((1,3,6,1,4,1,2,6,158,5,0,40))
ibmSpTrapCPUC.setObjects(*((_A,_B),(_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:ibmSpTrapCPUC.setStatus('')
ibmSpTrapMemoryC=NotificationType((1,3,6,1,4,1,2,6,158,5,0,41))
ibmSpTrapMemoryC.setObjects(*((_A,_B),(_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:ibmSpTrapMemoryC.setStatus('')
ibmSpTrapCPUN=NotificationType((1,3,6,1,4,1,2,6,158,5,0,42))
ibmSpTrapCPUN.setObjects(*((_A,_B),(_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:ibmSpTrapCPUN.setStatus('')
ibmSpTrapMemoryN=NotificationType((1,3,6,1,4,1,2,6,158,5,0,43))
ibmSpTrapMemoryN.setObjects(*((_A,_B),(_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:ibmSpTrapMemoryN.setStatus('')
ibmSpTrapHardwareC=NotificationType((1,3,6,1,4,1,2,6,158,5,0,50))
ibmSpTrapHardwareC.setObjects(*((_A,_B),(_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:ibmSpTrapHardwareC.setStatus('')
ibmSpTrapHardwareN=NotificationType((1,3,6,1,4,1,2,6,158,5,0,60))
ibmSpTrapHardwareN.setObjects(*((_A,_B),(_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:ibmSpTrapHardwareN.setStatus('')
ibmSpTrapPowerN=NotificationType((1,3,6,1,4,1,2,6,158,5,0,164))
ibmSpTrapPowerN.setObjects(*((_A,_B),(_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:ibmSpTrapPowerN.setStatus('')
ibmSpTrapFanN=NotificationType((1,3,6,1,4,1,2,6,158,5,0,165))
ibmSpTrapFanN.setObjects(*((_A,_B),(_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:ibmSpTrapFanN.setStatus('')
mibBuilder.exportSymbols(_A,**{'ibm':ibm,'ibmProd':ibmProd,'supportProcessor':supportProcessor,'immalertMIB':immalertMIB,'ibmSpTrapTempC':ibmSpTrapTempC,'ibmSpTrapVoltC':ibmSpTrapVoltC,'ibmSpTrapPowerC':ibmSpTrapPowerC,'ibmSpTrapHdC':ibmSpTrapHdC,'ibmSpTrapRdpsC':ibmSpTrapRdpsC,'ibmSpTrapRdpsN':ibmSpTrapRdpsN,'ibmSpTrapFanC':ibmSpTrapFanC,'ibmSpTrapTempN':ibmSpTrapTempN,'ibmSpTrapVoltN':ibmSpTrapVoltN,'ibmSpTrapOsToS':ibmSpTrapOsToS,'ibmSpTrapAppS':ibmSpTrapAppS,'ibmSpTrapPoffS':ibmSpTrapPoffS,'ibmSpTrapPonS':ibmSpTrapPonS,'ibmSpTrapBootS':ibmSpTrapBootS,'ibmSpTrapLdrToS':ibmSpTrapLdrToS,'ibmSpTrapPFAS':ibmSpTrapPFAS,'ibmSpTrapRLogin':ibmSpTrapRLogin,'ibmSpTrapSysLogS':ibmSpTrapSysLogS,'ibmSpTrapIhcC':ibmSpTrapIhcC,'ibmSpTrapNwChangeS':ibmSpTrapNwChangeS,'ibmSpTrapCPUC':ibmSpTrapCPUC,'ibmSpTrapMemoryC':ibmSpTrapMemoryC,'ibmSpTrapCPUN':ibmSpTrapCPUN,'ibmSpTrapMemoryN':ibmSpTrapMemoryN,'ibmSpTrapHardwareC':ibmSpTrapHardwareC,'ibmSpTrapHardwareN':ibmSpTrapHardwareN,'ibmSpTrapPowerN':ibmSpTrapPowerN,'ibmSpTrapFanN':ibmSpTrapFanN,'immtrapg':immtrapg,_B:altDateTime,_C:altSpTxtId,_D:altSysUuid,_E:altSysSern,_H:altPriority,_I:altMsgText,_F:altMsgID,_G:altMsgIDPrefix,_J:altHostContact,_K:altHostLocation,_L:altHostRoomID,_M:altHostRackID,_N:altHostLowestUpos,_O:altHostBladeBay,_P:altEventID,_Q:altServiceable,_R:altTest,_S:altFailingFRUs,_T:altHostMTM,_U:altAuxData,_V:altCommonEventID,_W:altEventType,_X:altDetectorID})