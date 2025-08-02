_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='DisplayString'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_B,'PhysAddress','TextualConvention')
tplinkDdmManageMIBObjects,=mibBuilder.importSymbols('TPLINK-DDMMANAGE-MIB','tplinkDdmManageMIBObjects')
ddmStatus=ModuleIdentity((1,3,6,1,4,1,11863,6,96,1,7))
if mibBuilder.loadTexts:ddmStatus.setRevisions(('2009-08-27 00:00',))
_DdmStatusTable_Object=MibTable
ddmStatusTable=_DdmStatusTable_Object((1,3,6,1,4,1,11863,6,96,1,7,1))
if mibBuilder.loadTexts:ddmStatusTable.setStatus(_A)
_DdmStatusEntry_Object=MibTableRow
ddmStatusEntry=_DdmStatusEntry_Object((1,3,6,1,4,1,11863,6,96,1,7,1,1))
ddmStatusEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:ddmStatusEntry.setStatus(_A)
class _DdmStatusPort_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DdmStatusPort_Type.__name__=_B
_DdmStatusPort_Object=MibTableColumn
ddmStatusPort=_DdmStatusPort_Object((1,3,6,1,4,1,11863,6,96,1,7,1,1,1),_DdmStatusPort_Type())
ddmStatusPort.setMaxAccess(_C)
if mibBuilder.loadTexts:ddmStatusPort.setStatus(_A)
class _DdmStatusTemperature_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DdmStatusTemperature_Type.__name__=_B
_DdmStatusTemperature_Object=MibTableColumn
ddmStatusTemperature=_DdmStatusTemperature_Object((1,3,6,1,4,1,11863,6,96,1,7,1,1,2),_DdmStatusTemperature_Type())
ddmStatusTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:ddmStatusTemperature.setStatus(_A)
class _DdmStatusVoltage_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DdmStatusVoltage_Type.__name__=_B
_DdmStatusVoltage_Object=MibTableColumn
ddmStatusVoltage=_DdmStatusVoltage_Object((1,3,6,1,4,1,11863,6,96,1,7,1,1,3),_DdmStatusVoltage_Type())
ddmStatusVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:ddmStatusVoltage.setStatus(_A)
class _DdmStatusBiasCurrent_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DdmStatusBiasCurrent_Type.__name__=_B
_DdmStatusBiasCurrent_Object=MibTableColumn
ddmStatusBiasCurrent=_DdmStatusBiasCurrent_Object((1,3,6,1,4,1,11863,6,96,1,7,1,1,4),_DdmStatusBiasCurrent_Type())
ddmStatusBiasCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:ddmStatusBiasCurrent.setStatus(_A)
class _DdmStatusTxPow_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DdmStatusTxPow_Type.__name__=_B
_DdmStatusTxPow_Object=MibTableColumn
ddmStatusTxPow=_DdmStatusTxPow_Object((1,3,6,1,4,1,11863,6,96,1,7,1,1,5),_DdmStatusTxPow_Type())
ddmStatusTxPow.setMaxAccess(_C)
if mibBuilder.loadTexts:ddmStatusTxPow.setStatus(_A)
class _DdmStatusRxPow_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DdmStatusRxPow_Type.__name__=_B
_DdmStatusRxPow_Object=MibTableColumn
ddmStatusRxPow=_DdmStatusRxPow_Object((1,3,6,1,4,1,11863,6,96,1,7,1,1,6),_DdmStatusRxPow_Type())
ddmStatusRxPow.setMaxAccess(_C)
if mibBuilder.loadTexts:ddmStatusRxPow.setStatus(_A)
class _DdmStatusDataReady_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DdmStatusDataReady_Type.__name__=_B
_DdmStatusDataReady_Object=MibTableColumn
ddmStatusDataReady=_DdmStatusDataReady_Object((1,3,6,1,4,1,11863,6,96,1,7,1,1,7),_DdmStatusDataReady_Type())
ddmStatusDataReady.setMaxAccess(_C)
if mibBuilder.loadTexts:ddmStatusDataReady.setStatus(_A)
class _DdmStatusLossSignal_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DdmStatusLossSignal_Type.__name__=_B
_DdmStatusLossSignal_Object=MibTableColumn
ddmStatusLossSignal=_DdmStatusLossSignal_Object((1,3,6,1,4,1,11863,6,96,1,7,1,1,8),_DdmStatusLossSignal_Type())
ddmStatusLossSignal.setMaxAccess(_C)
if mibBuilder.loadTexts:ddmStatusLossSignal.setStatus(_A)
class _DdmStatusTxFault_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DdmStatusTxFault_Type.__name__=_B
_DdmStatusTxFault_Object=MibTableColumn
ddmStatusTxFault=_DdmStatusTxFault_Object((1,3,6,1,4,1,11863,6,96,1,7,1,1,9),_DdmStatusTxFault_Type())
ddmStatusTxFault.setMaxAccess(_C)
if mibBuilder.loadTexts:ddmStatusTxFault.setStatus(_A)
mibBuilder.exportSymbols('TPLINK-DDMSTATUS-MIB',**{'ddmStatus':ddmStatus,'ddmStatusTable':ddmStatusTable,'ddmStatusEntry':ddmStatusEntry,'ddmStatusPort':ddmStatusPort,'ddmStatusTemperature':ddmStatusTemperature,'ddmStatusVoltage':ddmStatusVoltage,'ddmStatusBiasCurrent':ddmStatusBiasCurrent,'ddmStatusTxPow':ddmStatusTxPow,'ddmStatusRxPow':ddmStatusRxPow,'ddmStatusDataReady':ddmStatusDataReady,'ddmStatusLossSignal':ddmStatusLossSignal,'ddmStatusTxFault':ddmStatusTxFault})