_P='ciscoOpticalMonMIBParamGroup'
_O='comRxPowerAC'
_N='comRxPowerACSupported'
_M='comRxPowerACDC'
_L='comTxLaserTemp'
_K='comTxLaserTempSupported'
_J='comTxPower'
_I='comTxPowerSupported'
_H='comTxBiasCurrent'
_G='ifIndex'
_F='IF-MIB'
_E='microWatts'
_D='Integer32'
_C='read-only'
_B='CISCO-OPTICAL-MONITORING-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
ifIndex,=mibBuilder.importSymbols(_F,_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
ciscoOpticalMonitoringMIB=ModuleIdentity((1,3,6,1,4,1,9,10,83))
if mibBuilder.loadTexts:ciscoOpticalMonitoringMIB.setRevisions(('2001-12-04 11:30',))
_CiscoOpticalMonMIBObjects_ObjectIdentity=ObjectIdentity
ciscoOpticalMonMIBObjects=_CiscoOpticalMonMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,10,83,1))
_ComParameters_ObjectIdentity=ObjectIdentity
comParameters=_ComParameters_ObjectIdentity((1,3,6,1,4,1,9,10,83,1,1))
_ComParametersTable_Object=MibTable
comParametersTable=_ComParametersTable_Object((1,3,6,1,4,1,9,10,83,1,1,1))
if mibBuilder.loadTexts:comParametersTable.setStatus(_A)
_ComParametersEntry_Object=MibTableRow
comParametersEntry=_ComParametersEntry_Object((1,3,6,1,4,1,9,10,83,1,1,1,1))
comParametersEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:comParametersEntry.setStatus(_A)
class _ComTxBiasCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_ComTxBiasCurrent_Type.__name__=_D
_ComTxBiasCurrent_Object=MibTableColumn
comTxBiasCurrent=_ComTxBiasCurrent_Object((1,3,6,1,4,1,9,10,83,1,1,1,1,1),_ComTxBiasCurrent_Type())
comTxBiasCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:comTxBiasCurrent.setStatus(_A)
if mibBuilder.loadTexts:comTxBiasCurrent.setUnits('milliamps')
_ComTxPowerSupported_Type=TruthValue
_ComTxPowerSupported_Object=MibTableColumn
comTxPowerSupported=_ComTxPowerSupported_Object((1,3,6,1,4,1,9,10,83,1,1,1,1,2),_ComTxPowerSupported_Type())
comTxPowerSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:comTxPowerSupported.setStatus(_A)
class _ComTxPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_ComTxPower_Type.__name__=_D
_ComTxPower_Object=MibTableColumn
comTxPower=_ComTxPower_Object((1,3,6,1,4,1,9,10,83,1,1,1,1,3),_ComTxPower_Type())
comTxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:comTxPower.setStatus(_A)
if mibBuilder.loadTexts:comTxPower.setUnits(_E)
_ComTxLaserTempSupported_Type=TruthValue
_ComTxLaserTempSupported_Object=MibTableColumn
comTxLaserTempSupported=_ComTxLaserTempSupported_Object((1,3,6,1,4,1,9,10,83,1,1,1,1,4),_ComTxLaserTempSupported_Type())
comTxLaserTempSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:comTxLaserTempSupported.setStatus(_A)
class _ComTxLaserTemp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-253,200))
_ComTxLaserTemp_Type.__name__=_D
_ComTxLaserTemp_Object=MibTableColumn
comTxLaserTemp=_ComTxLaserTemp_Object((1,3,6,1,4,1,9,10,83,1,1,1,1,5),_ComTxLaserTemp_Type())
comTxLaserTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:comTxLaserTemp.setStatus(_A)
if mibBuilder.loadTexts:comTxLaserTemp.setUnits(' Degree Centigrade')
class _ComRxPowerACDC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_ComRxPowerACDC_Type.__name__=_D
_ComRxPowerACDC_Object=MibTableColumn
comRxPowerACDC=_ComRxPowerACDC_Object((1,3,6,1,4,1,9,10,83,1,1,1,1,6),_ComRxPowerACDC_Type())
comRxPowerACDC.setMaxAccess(_C)
if mibBuilder.loadTexts:comRxPowerACDC.setStatus(_A)
if mibBuilder.loadTexts:comRxPowerACDC.setUnits(_E)
_ComRxPowerACSupported_Type=TruthValue
_ComRxPowerACSupported_Object=MibTableColumn
comRxPowerACSupported=_ComRxPowerACSupported_Object((1,3,6,1,4,1,9,10,83,1,1,1,1,7),_ComRxPowerACSupported_Type())
comRxPowerACSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:comRxPowerACSupported.setStatus(_A)
class _ComRxPowerAC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_ComRxPowerAC_Type.__name__=_D
_ComRxPowerAC_Object=MibTableColumn
comRxPowerAC=_ComRxPowerAC_Object((1,3,6,1,4,1,9,10,83,1,1,1,1,8),_ComRxPowerAC_Type())
comRxPowerAC.setMaxAccess(_C)
if mibBuilder.loadTexts:comRxPowerAC.setStatus(_A)
if mibBuilder.loadTexts:comRxPowerAC.setUnits(_E)
_CiscoOpticalMonMIBNotifPrefix_ObjectIdentity=ObjectIdentity
ciscoOpticalMonMIBNotifPrefix=_CiscoOpticalMonMIBNotifPrefix_ObjectIdentity((1,3,6,1,4,1,9,10,83,2))
_CiscoOpticalMonMIBNotifications_ObjectIdentity=ObjectIdentity
ciscoOpticalMonMIBNotifications=_CiscoOpticalMonMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,10,83,2,0))
_CiscoOpticalMonMIBConformance_ObjectIdentity=ObjectIdentity
ciscoOpticalMonMIBConformance=_CiscoOpticalMonMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,10,83,3))
_CiscoOpticalMonMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoOpticalMonMIBCompliances=_CiscoOpticalMonMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,83,3,1))
_CiscoOpticalMonMIBGroups_ObjectIdentity=ObjectIdentity
ciscoOpticalMonMIBGroups=_CiscoOpticalMonMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,10,83,3,2))
ciscoOpticalMonMIBParamGroup=ObjectGroup((1,3,6,1,4,1,9,10,83,3,2,1))
ciscoOpticalMonMIBParamGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:ciscoOpticalMonMIBParamGroup.setStatus(_A)
ciscoOpticalMonMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,83,3,1,1))
ciscoOpticalMonMIBCompliance.setObjects((_B,_P))
if mibBuilder.loadTexts:ciscoOpticalMonMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoOpticalMonitoringMIB':ciscoOpticalMonitoringMIB,'ciscoOpticalMonMIBObjects':ciscoOpticalMonMIBObjects,'comParameters':comParameters,'comParametersTable':comParametersTable,'comParametersEntry':comParametersEntry,_H:comTxBiasCurrent,_I:comTxPowerSupported,_J:comTxPower,_K:comTxLaserTempSupported,_L:comTxLaserTemp,_M:comRxPowerACDC,_N:comRxPowerACSupported,_O:comRxPowerAC,'ciscoOpticalMonMIBNotifPrefix':ciscoOpticalMonMIBNotifPrefix,'ciscoOpticalMonMIBNotifications':ciscoOpticalMonMIBNotifications,'ciscoOpticalMonMIBConformance':ciscoOpticalMonMIBConformance,'ciscoOpticalMonMIBCompliances':ciscoOpticalMonMIBCompliances,'ciscoOpticalMonMIBCompliance':ciscoOpticalMonMIBCompliance,'ciscoOpticalMonMIBGroups':ciscoOpticalMonMIBGroups,_P:ciscoOpticalMonMIBParamGroup})