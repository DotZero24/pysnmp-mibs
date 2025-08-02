_L='PhysAddress'
_K='TimeTicks'
_J='NotificationType'
_I='IpAddress'
_H='Gauge32'
_G='Counter32'
_F='ifIndex'
_E='IF-MIB'
_D='DisplayString'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits',_G,'Counter64',_H,_C,_I,'ModuleIdentity','MibIdentifier',_J,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_J,_K,'Unsigned32','enterprises','iso')
Counter32,Gauge32,Integer32,IpAddress,TimeTicks=mibBuilder.importSymbols('SNMPv2-SMI-v1',_G,_H,_C,_I,_K)
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,_L,'TextualConvention')
AutonomousType,DisplayString,PhysAddress,RowStatus,TestAndIncr,TruthValue=mibBuilder.importSymbols('SNMPv2-TC-v1','AutonomousType',_D,_L,'RowStatus','TestAndIncr','TruthValue')
_Ibm_ObjectIdentity=ObjectIdentity
ibm=_Ibm_ObjectIdentity((1,3,6,1,4,1,2))
_IbmProd_ObjectIdentity=ObjectIdentity
ibmProd=_IbmProd_ObjectIdentity((1,3,6,1,4,1,2,6))
_Ibm2210_ObjectIdentity=ObjectIdentity
ibm2210=_Ibm2210_ObjectIdentity((1,3,6,1,4,1,2,6,72))
_IbmIROC_ObjectIdentity=ObjectIdentity
ibmIROC=_IbmIROC_ObjectIdentity((1,3,6,1,4,1,2,6,119))
_IbmIROCrouting_ObjectIdentity=ObjectIdentity
ibmIROCrouting=_IbmIROCrouting_ObjectIdentity((1,3,6,1,4,1,2,6,119,4))
_IbmIROCroutingDialOut_ObjectIdentity=ObjectIdentity
ibmIROCroutingDialOut=_IbmIROCroutingDialOut_ObjectIdentity((1,3,6,1,4,1,2,6,119,4,6))
_IbmDialOutTraps_ObjectIdentity=ObjectIdentity
ibmDialOutTraps=_IbmDialOutTraps_ObjectIdentity((1,3,6,1,4,1,2,6,119,4,6,0))
_IbmDialOutMIB_ObjectIdentity=ObjectIdentity
ibmDialOutMIB=_IbmDialOutMIB_ObjectIdentity((1,3,6,1,4,1,2,6,119,4,6,1))
_IbmDialOutGeneral_ObjectIdentity=ObjectIdentity
ibmDialOutGeneral=_IbmDialOutGeneral_ObjectIdentity((1,3,6,1,4,1,2,6,119,4,6,1,1))
_DialOutIfTable_Object=MibTable
dialOutIfTable=_DialOutIfTable_Object((1,3,6,1,4,1,2,6,119,4,6,1,2))
if mibBuilder.loadTexts:dialOutIfTable.setStatus(_A)
_DialOutIfEntry_Object=MibTableRow
dialOutIfEntry=_DialOutIfEntry_Object((1,3,6,1,4,1,2,6,119,4,6,1,2,1))
dialOutIfEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:dialOutIfEntry.setStatus(_A)
class _DialOutIfUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,253))
_DialOutIfUserName_Type.__name__=_D
_DialOutIfUserName_Object=MibTableColumn
dialOutIfUserName=_DialOutIfUserName_Object((1,3,6,1,4,1,2,6,119,4,6,1,2,1,1),_DialOutIfUserName_Type())
dialOutIfUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:dialOutIfUserName.setStatus(_A)
class _DialOutIfTimeRemaining_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_DialOutIfTimeRemaining_Type.__name__=_C
_DialOutIfTimeRemaining_Object=MibTableColumn
dialOutIfTimeRemaining=_DialOutIfTimeRemaining_Object((1,3,6,1,4,1,2,6,119,4,6,1,2,1,2),_DialOutIfTimeRemaining_Type())
dialOutIfTimeRemaining.setMaxAccess(_B)
if mibBuilder.loadTexts:dialOutIfTimeRemaining.setStatus(_A)
class _DialOutIfInactivityTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_DialOutIfInactivityTimer_Type.__name__=_C
_DialOutIfInactivityTimer_Object=MibTableColumn
dialOutIfInactivityTimer=_DialOutIfInactivityTimer_Object((1,3,6,1,4,1,2,6,119,4,6,1,2,1,3),_DialOutIfInactivityTimer_Type())
dialOutIfInactivityTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:dialOutIfInactivityTimer.setStatus(_A)
class _DialOutIfDTRState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('noChange',0),('on',1),('off',2)))
_DialOutIfDTRState_Type.__name__=_C
_DialOutIfDTRState_Object=MibTableColumn
dialOutIfDTRState=_DialOutIfDTRState_Object((1,3,6,1,4,1,2,6,119,4,6,1,2,1,4),_DialOutIfDTRState_Type())
dialOutIfDTRState.setMaxAccess(_B)
if mibBuilder.loadTexts:dialOutIfDTRState.setStatus(_A)
class _DialOutIfProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('undefined',1),('hose',2),('telnet',3)))
_DialOutIfProtocol_Type.__name__=_C
_DialOutIfProtocol_Object=MibTableColumn
dialOutIfProtocol=_DialOutIfProtocol_Object((1,3,6,1,4,1,2,6,119,4,6,1,2,1,5),_DialOutIfProtocol_Type())
dialOutIfProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:dialOutIfProtocol.setStatus(_A)
_DialOutEnableComport_Type=TruthValue
_DialOutEnableComport_Object=MibTableColumn
dialOutEnableComport=_DialOutEnableComport_Object((1,3,6,1,4,1,2,6,119,4,6,1,2,1,6),_DialOutEnableComport_Type())
dialOutEnableComport.setMaxAccess(_B)
if mibBuilder.loadTexts:dialOutEnableComport.setStatus(_A)
_DialOutSendBinary_Type=TruthValue
_DialOutSendBinary_Object=MibTableColumn
dialOutSendBinary=_DialOutSendBinary_Object((1,3,6,1,4,1,2,6,119,4,6,1,2,1,7),_DialOutSendBinary_Type())
dialOutSendBinary.setMaxAccess(_B)
if mibBuilder.loadTexts:dialOutSendBinary.setStatus(_A)
_DialOutSupressGoAhead_Type=TruthValue
_DialOutSupressGoAhead_Object=MibTableColumn
dialOutSupressGoAhead=_DialOutSupressGoAhead_Object((1,3,6,1,4,1,2,6,119,4,6,1,2,1,8),_DialOutSupressGoAhead_Type())
dialOutSupressGoAhead.setMaxAccess(_B)
if mibBuilder.loadTexts:dialOutSupressGoAhead.setStatus(_A)
_DialOutDisableEcho_Type=TruthValue
_DialOutDisableEcho_Object=MibTableColumn
dialOutDisableEcho=_DialOutDisableEcho_Object((1,3,6,1,4,1,2,6,119,4,6,1,2,1,9),_DialOutDisableEcho_Type())
dialOutDisableEcho.setMaxAccess(_B)
if mibBuilder.loadTexts:dialOutDisableEcho.setStatus(_A)
class _DialOutPortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DialOutPortName_Type.__name__=_D
_DialOutPortName_Object=MibTableColumn
dialOutPortName=_DialOutPortName_Object((1,3,6,1,4,1,2,6,119,4,6,1,2,1,10),_DialOutPortName_Type())
dialOutPortName.setMaxAccess('read-write')
if mibBuilder.loadTexts:dialOutPortName.setStatus(_A)
_IbmDialOutDomains_ObjectIdentity=ObjectIdentity
ibmDialOutDomains=_IbmDialOutDomains_ObjectIdentity((1,3,6,1,4,1,2,6,119,4,6,2))
_IbmDialOutConformance_ObjectIdentity=ObjectIdentity
ibmDialOutConformance=_IbmDialOutConformance_ObjectIdentity((1,3,6,1,4,1,2,6,119,4,6,3))
_DialOutCompliances_ObjectIdentity=ObjectIdentity
dialOutCompliances=_DialOutCompliances_ObjectIdentity((1,3,6,1,4,1,2,6,119,4,6,3,1))
_DialOutCoreCompliance_ObjectIdentity=ObjectIdentity
dialOutCoreCompliance=_DialOutCoreCompliance_ObjectIdentity((1,3,6,1,4,1,2,6,119,4,6,3,1,1))
_DialOutGroups_ObjectIdentity=ObjectIdentity
dialOutGroups=_DialOutGroups_ObjectIdentity((1,3,6,1,4,1,2,6,119,4,6,3,2))
_DialOutIfGroup_ObjectIdentity=ObjectIdentity
dialOutIfGroup=_DialOutIfGroup_ObjectIdentity((1,3,6,1,4,1,2,6,119,4,6,3,2,1))
mibBuilder.exportSymbols('IBMIROCDIALOUT-MIB',**{'ibm':ibm,'ibmProd':ibmProd,'ibm2210':ibm2210,'ibmIROC':ibmIROC,'ibmIROCrouting':ibmIROCrouting,'ibmIROCroutingDialOut':ibmIROCroutingDialOut,'ibmDialOutTraps':ibmDialOutTraps,'ibmDialOutMIB':ibmDialOutMIB,'ibmDialOutGeneral':ibmDialOutGeneral,'dialOutIfTable':dialOutIfTable,'dialOutIfEntry':dialOutIfEntry,'dialOutIfUserName':dialOutIfUserName,'dialOutIfTimeRemaining':dialOutIfTimeRemaining,'dialOutIfInactivityTimer':dialOutIfInactivityTimer,'dialOutIfDTRState':dialOutIfDTRState,'dialOutIfProtocol':dialOutIfProtocol,'dialOutEnableComport':dialOutEnableComport,'dialOutSendBinary':dialOutSendBinary,'dialOutSupressGoAhead':dialOutSupressGoAhead,'dialOutDisableEcho':dialOutDisableEcho,'dialOutPortName':dialOutPortName,'ibmDialOutDomains':ibmDialOutDomains,'ibmDialOutConformance':ibmDialOutConformance,'dialOutCompliances':dialOutCompliances,'dialOutCoreCompliance':dialOutCoreCompliance,'dialOutGroups':dialOutGroups,'dialOutIfGroup':dialOutIfGroup})