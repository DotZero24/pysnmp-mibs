_V='cpqSwccEmuDevEventDescription'
_U='cpqSwccEmuDevDevState'
_T='cpqSwccEmuDevDevName'
_S='NotificationType'
_R='cpqSwccKzpccSubsystemName'
_Q='cpqSwccKzpccSystemName'
_P='cpqSwccFibreEventDescription'
_O='cpqSwccFibreDevState'
_N='cpqSwccFibreDevName'
_M='failed'
_L='degraded'
_K='other'
_J='cpqSwccKzpccEventDescription'
_I='cpqSwccKzpccEventSeverity'
_H='not-accessible'
_G='sysName'
_F='SNMPv2-MIB'
_E='DisplayString'
_D='Integer32'
_C='read-only'
_B='mandatory'
_A='CPQSWCC-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
compaq,cpqHoTrapFlags=mibBuilder.importSymbols('CPQHOST-MIB','compaq','cpqHoTrapFlags')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols(_F,_G)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier',_S,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_S,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
_CpqSwcc_ObjectIdentity=ObjectIdentity
cpqSwcc=_CpqSwcc_ObjectIdentity((1,3,6,1,4,1,232,132))
_CpqSwccMibRev_ObjectIdentity=ObjectIdentity
cpqSwccMibRev=_CpqSwccMibRev_ObjectIdentity((1,3,6,1,4,1,232,132,1))
class _CpqSwccMibRevMajor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CpqSwccMibRevMajor_Type.__name__=_D
_CpqSwccMibRevMajor_Object=MibScalar
cpqSwccMibRevMajor=_CpqSwccMibRevMajor_Object((1,3,6,1,4,1,232,132,1,1),_CpqSwccMibRevMajor_Type())
cpqSwccMibRevMajor.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSwccMibRevMajor.setStatus(_B)
class _CpqSwccMibRevMinor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSwccMibRevMinor_Type.__name__=_D
_CpqSwccMibRevMinor_Object=MibScalar
cpqSwccMibRevMinor=_CpqSwccMibRevMinor_Object((1,3,6,1,4,1,232,132,1,2),_CpqSwccMibRevMinor_Type())
cpqSwccMibRevMinor.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSwccMibRevMinor.setStatus(_B)
class _CpqSwccMibCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),('ok',2),(_L,3),(_M,4)))
_CpqSwccMibCondition_Type.__name__=_D
_CpqSwccMibCondition_Object=MibScalar
cpqSwccMibCondition=_CpqSwccMibCondition_Object((1,3,6,1,4,1,232,132,1,3),_CpqSwccMibCondition_Type())
cpqSwccMibCondition.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSwccMibCondition.setStatus(_B)
_CpqSwccFibre_ObjectIdentity=ObjectIdentity
cpqSwccFibre=_CpqSwccFibre_ObjectIdentity((1,3,6,1,4,1,232,132,2))
class _CpqSwccFibreDevName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CpqSwccFibreDevName_Type.__name__=_E
_CpqSwccFibreDevName_Object=MibScalar
cpqSwccFibreDevName=_CpqSwccFibreDevName_Object((1,3,6,1,4,1,232,132,2,1),_CpqSwccFibreDevName_Type())
cpqSwccFibreDevName.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSwccFibreDevName.setStatus(_B)
class _CpqSwccFibreDevState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),('ok',2),(_L,3),(_M,4)))
_CpqSwccFibreDevState_Type.__name__=_D
_CpqSwccFibreDevState_Object=MibScalar
cpqSwccFibreDevState=_CpqSwccFibreDevState_Object((1,3,6,1,4,1,232,132,2,2),_CpqSwccFibreDevState_Type())
cpqSwccFibreDevState.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSwccFibreDevState.setStatus(_B)
class _CpqSwccFibreEventDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_CpqSwccFibreEventDescription_Type.__name__=_E
_CpqSwccFibreEventDescription_Object=MibScalar
cpqSwccFibreEventDescription=_CpqSwccFibreEventDescription_Object((1,3,6,1,4,1,232,132,2,3),_CpqSwccFibreEventDescription_Type())
cpqSwccFibreEventDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSwccFibreEventDescription.setStatus(_B)
_CpqSwccEmuDev_ObjectIdentity=ObjectIdentity
cpqSwccEmuDev=_CpqSwccEmuDev_ObjectIdentity((1,3,6,1,4,1,232,132,3))
class _CpqSwccEmuDevDevName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CpqSwccEmuDevDevName_Type.__name__=_E
_CpqSwccEmuDevDevName_Object=MibScalar
cpqSwccEmuDevDevName=_CpqSwccEmuDevDevName_Object((1,3,6,1,4,1,232,132,3,1),_CpqSwccEmuDevDevName_Type())
cpqSwccEmuDevDevName.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSwccEmuDevDevName.setStatus(_B)
class _CpqSwccEmuDevDevState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),('ok',2),(_L,3),(_M,4)))
_CpqSwccEmuDevDevState_Type.__name__=_D
_CpqSwccEmuDevDevState_Object=MibScalar
cpqSwccEmuDevDevState=_CpqSwccEmuDevDevState_Object((1,3,6,1,4,1,232,132,3,2),_CpqSwccEmuDevDevState_Type())
cpqSwccEmuDevDevState.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSwccEmuDevDevState.setStatus(_B)
class _CpqSwccEmuDevEventDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_CpqSwccEmuDevEventDescription_Type.__name__=_E
_CpqSwccEmuDevEventDescription_Object=MibScalar
cpqSwccEmuDevEventDescription=_CpqSwccEmuDevEventDescription_Object((1,3,6,1,4,1,232,132,3,3),_CpqSwccEmuDevEventDescription_Type())
cpqSwccEmuDevEventDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSwccEmuDevEventDescription.setStatus(_B)
_CpqSwccKzpcc_ObjectIdentity=ObjectIdentity
cpqSwccKzpcc=_CpqSwccKzpcc_ObjectIdentity((1,3,6,1,4,1,232,132,4))
_CpqSwccKzpccTrap_ObjectIdentity=ObjectIdentity
cpqSwccKzpccTrap=_CpqSwccKzpccTrap_ObjectIdentity((1,3,6,1,4,1,232,132,4,1))
_CpqSwccKzpccSytemName_Type=OctetString
_CpqSwccKzpccSytemName_Object=MibScalar
cpqSwccKzpccSytemName=_CpqSwccKzpccSytemName_Object((1,3,6,1,4,1,232,132,4,1,1),_CpqSwccKzpccSytemName_Type())
cpqSwccKzpccSytemName.setMaxAccess(_H)
if mibBuilder.loadTexts:cpqSwccKzpccSytemName.setStatus(_B)
_CpqSwccKzpccSubsytemName_Type=OctetString
_CpqSwccKzpccSubsytemName_Object=MibScalar
cpqSwccKzpccSubsytemName=_CpqSwccKzpccSubsytemName_Object((1,3,6,1,4,1,232,132,4,1,2),_CpqSwccKzpccSubsytemName_Type())
cpqSwccKzpccSubsytemName.setMaxAccess(_H)
if mibBuilder.loadTexts:cpqSwccKzpccSubsytemName.setStatus(_B)
class _CpqSwccKzpccEventSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('informational',1),('warning',2),('error',3)))
_CpqSwccKzpccEventSeverity_Type.__name__=_D
_CpqSwccKzpccEventSeverity_Object=MibScalar
cpqSwccKzpccEventSeverity=_CpqSwccKzpccEventSeverity_Object((1,3,6,1,4,1,232,132,4,1,3),_CpqSwccKzpccEventSeverity_Type())
cpqSwccKzpccEventSeverity.setMaxAccess(_H)
if mibBuilder.loadTexts:cpqSwccKzpccEventSeverity.setStatus(_B)
_CpqSwccKzpccEventDescription_Type=OctetString
_CpqSwccKzpccEventDescription_Object=MibScalar
cpqSwccKzpccEventDescription=_CpqSwccKzpccEventDescription_Object((1,3,6,1,4,1,232,132,4,1,4),_CpqSwccKzpccEventDescription_Type())
cpqSwccKzpccEventDescription.setMaxAccess(_H)
if mibBuilder.loadTexts:cpqSwccKzpccEventDescription.setStatus(_B)
cpqSwccFibreDeviceStatusChange=NotificationType((1,3,6,1,4,1,232,132,2,0,1))
cpqSwccFibreDeviceStatusChange.setObjects(*((_F,_G),(_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:cpqSwccFibreDeviceStatusChange.setStatus('')
cpqSwccTapeControllerStatusChange=NotificationType((1,3,6,1,4,1,232,132,2,0,2))
cpqSwccTapeControllerStatusChange.setObjects(*((_F,_G),(_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:cpqSwccTapeControllerStatusChange.setStatus('')
cpqSwccEmuDevDeviceStatusChange=NotificationType((1,3,6,1,4,1,232,132,3,0,1))
cpqSwccEmuDevDeviceStatusChange.setObjects(*((_F,_G),(_A,_T),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:cpqSwccEmuDevDeviceStatusChange.setStatus('')
cpqSwccKzpccPhyDeviceEventTrap=NotificationType((1,3,6,1,4,1,232,132,4,1,0,1))
cpqSwccKzpccPhyDeviceEventTrap.setObjects(*((_A,_Q),(_A,_R),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:cpqSwccKzpccPhyDeviceEventTrap.setStatus('')
cpqSwccKzpccVirtualDeviceEventTrap=NotificationType((1,3,6,1,4,1,232,132,4,1,0,2))
cpqSwccKzpccVirtualDeviceEventTrap.setObjects(*((_A,_Q),(_A,_R),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:cpqSwccKzpccVirtualDeviceEventTrap.setStatus('')
cpqSwccKzpccSubsystemEventTrap=NotificationType((1,3,6,1,4,1,232,132,4,1,0,3))
cpqSwccKzpccSubsystemEventTrap.setObjects(*((_A,_Q),(_A,_R),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:cpqSwccKzpccSubsystemEventTrap.setStatus('')
mibBuilder.exportSymbols(_A,**{'cpqSwcc':cpqSwcc,'cpqSwccMibRev':cpqSwccMibRev,'cpqSwccMibRevMajor':cpqSwccMibRevMajor,'cpqSwccMibRevMinor':cpqSwccMibRevMinor,'cpqSwccMibCondition':cpqSwccMibCondition,'cpqSwccFibre':cpqSwccFibre,'cpqSwccFibreDeviceStatusChange':cpqSwccFibreDeviceStatusChange,'cpqSwccTapeControllerStatusChange':cpqSwccTapeControllerStatusChange,_N:cpqSwccFibreDevName,_O:cpqSwccFibreDevState,_P:cpqSwccFibreEventDescription,'cpqSwccEmuDev':cpqSwccEmuDev,'cpqSwccEmuDevDeviceStatusChange':cpqSwccEmuDevDeviceStatusChange,_T:cpqSwccEmuDevDevName,_U:cpqSwccEmuDevDevState,_V:cpqSwccEmuDevEventDescription,'cpqSwccKzpcc':cpqSwccKzpcc,'cpqSwccKzpccTrap':cpqSwccKzpccTrap,'cpqSwccKzpccPhyDeviceEventTrap':cpqSwccKzpccPhyDeviceEventTrap,'cpqSwccKzpccVirtualDeviceEventTrap':cpqSwccKzpccVirtualDeviceEventTrap,'cpqSwccKzpccSubsystemEventTrap':cpqSwccKzpccSubsystemEventTrap,'cpqSwccKzpccSytemName':cpqSwccKzpccSytemName,'cpqSwccKzpccSubsytemName':cpqSwccKzpccSubsytemName,_I:cpqSwccKzpccEventSeverity,_J:cpqSwccKzpccEventDescription})