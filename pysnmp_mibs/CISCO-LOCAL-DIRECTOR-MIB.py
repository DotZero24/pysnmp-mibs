_AD='ciscoLocalDirectorFailoverGroup'
_AC='ciscoLocalDirectorExVirtualStateChange'
_AB='ciscoLocalDirectorEVirtualStateChange'
_AA='ciscoLocalDirectorRealStateChange'
_A9='ciscoLocalDirectorVirtualStateChange'
_A8='cldexVirtualWeight'
_A7='cldexVirtualTotalBytes'
_A6='cldexVirtualTotalPackets'
_A5='cldexVirtualTotalConnections'
_A4='cldeVirtualWeight'
_A3='cldeVirtualTotalBytes'
_A2='cldeVirtualTotalPackets'
_A1='cldeVirtualTotalConnections'
_A0='cldFailoverActiveTimeStamp'
_z='cldFailoverUnitType'
_y='cldRealWeight'
_x='cldRealTotalBytes'
_w='cldRealTotalPackets'
_v='cldRealTotalConnections'
_u='cldVirtualWeight'
_t='cldVirtualTotalBytes'
_s='cldVirtualTotalPackets'
_r='cldVirtualTotalConnections'
_q='cldeRealProtocol'
_p='cldeRealBindID'
_o='cldeRealPort'
_n='cldeRealIpAddress'
_m='read-write'
_l='cldRealPort'
_k='cldRealIpAddress'
_j='cldexVirtualRule'
_i='cldexVirtualProtocol'
_h='cldexVirtualBindID'
_g='cldexVirtualPort'
_f='cldexVirtualIpAddress'
_e='cldeVirtualProtocol'
_d='cldeVirtualBindID'
_c='cldeVirtualPort'
_b='cldeVirtualIpAddress'
_a='cldVirtualBindID'
_Z='cldVirtualPort'
_Y='cldVirtualIpAddress'
_X='SnmpAdminString'
_W='ciscoLocalDirectorERealStateChange'
_V='ciscoLocalDirectorFailoverUnitStatus'
_U='cldexVirtualState'
_T='cldeRealWeight'
_S='cldeRealTotalBytes'
_R='cldeRealTotalPackets'
_Q='cldeRealTotalConnections'
_P='cldeVirtualState'
_O='cldFailoverUnitStatus'
_N='cldFailoverCableStatus'
_M='cldFailoverEnabled'
_L='cldRealState'
_K='cldVirtualState'
_J='ciscoLocalDirectorFailoverCableChange'
_I='ciscoLocalDirectorFailoverEnableChange'
_H='cldeRealState'
_G='Integer32'
_F='deprecated'
_E='not-accessible'
_D='obsolete'
_C='read-only'
_B='current'
_A='CISCO-LOCAL-DIRECTOR-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_X)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
ciscoLocalDirectorMIB=ModuleIdentity((1,3,6,1,4,1,9,9,99))
if mibBuilder.loadTexts:ciscoLocalDirectorMIB.setRevisions(('2001-05-14 00:00','1999-10-21 00:00','1999-02-05 00:00'))
class CldMachineState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('inService',1),('outOfService',2),('testing',3),('failed',4),('maxCapacity',5),('maintenance',6),('stickyOnly',7),('externalFailed',8)))
class CldFailoverEnabledState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('failoverOn',1),('failoverOff',2)))
class CldFailoverCableState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('normalConnected',1),('otherSidePoweredOff',2),('mySideNotConnected',3),('otherSideNotConnected',4),('badCable',5)))
class CldFailoverUnitTypeDescriptor(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('primary',1),('secondary',2)))
class CldFailoverUnitStatusDescriptor(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('standby',2)))
class MachineProtocol(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,6,17,47)));namedValues=NamedValues(*(('protocolTypeAll',0),('protocolTypeTCP',6),('protocolTypeUDP',17),('protocolTypeGRE',47)))
class MachineBindID(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CiscoLocalDirectorMIBObjects_ObjectIdentity=ObjectIdentity
ciscoLocalDirectorMIBObjects=_CiscoLocalDirectorMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,99,1))
_CldVirtualMachine_ObjectIdentity=ObjectIdentity
cldVirtualMachine=_CldVirtualMachine_ObjectIdentity((1,3,6,1,4,1,9,9,99,1,1))
_CldVirtualTable_Object=MibTable
cldVirtualTable=_CldVirtualTable_Object((1,3,6,1,4,1,9,9,99,1,1,1))
if mibBuilder.loadTexts:cldVirtualTable.setStatus(_D)
_CldVirtualTableEntry_Object=MibTableRow
cldVirtualTableEntry=_CldVirtualTableEntry_Object((1,3,6,1,4,1,9,9,99,1,1,1,1))
cldVirtualTableEntry.setIndexNames((0,_A,_Y),(0,_A,_Z),(0,_A,_a))
if mibBuilder.loadTexts:cldVirtualTableEntry.setStatus(_D)
_CldVirtualIpAddress_Type=IpAddress
_CldVirtualIpAddress_Object=MibTableColumn
cldVirtualIpAddress=_CldVirtualIpAddress_Object((1,3,6,1,4,1,9,9,99,1,1,1,1,1),_CldVirtualIpAddress_Type())
cldVirtualIpAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:cldVirtualIpAddress.setStatus(_D)
class _CldVirtualPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CldVirtualPort_Type.__name__=_G
_CldVirtualPort_Object=MibTableColumn
cldVirtualPort=_CldVirtualPort_Object((1,3,6,1,4,1,9,9,99,1,1,1,1,2),_CldVirtualPort_Type())
cldVirtualPort.setMaxAccess(_E)
if mibBuilder.loadTexts:cldVirtualPort.setStatus(_D)
class _CldVirtualBindID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CldVirtualBindID_Type.__name__=_G
_CldVirtualBindID_Object=MibTableColumn
cldVirtualBindID=_CldVirtualBindID_Object((1,3,6,1,4,1,9,9,99,1,1,1,1,3),_CldVirtualBindID_Type())
cldVirtualBindID.setMaxAccess(_E)
if mibBuilder.loadTexts:cldVirtualBindID.setStatus(_D)
_CldVirtualState_Type=CldMachineState
_CldVirtualState_Object=MibTableColumn
cldVirtualState=_CldVirtualState_Object((1,3,6,1,4,1,9,9,99,1,1,1,1,4),_CldVirtualState_Type())
cldVirtualState.setMaxAccess(_C)
if mibBuilder.loadTexts:cldVirtualState.setStatus(_D)
_CldVirtualTotalConnections_Type=Counter32
_CldVirtualTotalConnections_Object=MibTableColumn
cldVirtualTotalConnections=_CldVirtualTotalConnections_Object((1,3,6,1,4,1,9,9,99,1,1,1,1,5),_CldVirtualTotalConnections_Type())
cldVirtualTotalConnections.setMaxAccess(_C)
if mibBuilder.loadTexts:cldVirtualTotalConnections.setStatus(_D)
_CldVirtualTotalPackets_Type=Counter32
_CldVirtualTotalPackets_Object=MibTableColumn
cldVirtualTotalPackets=_CldVirtualTotalPackets_Object((1,3,6,1,4,1,9,9,99,1,1,1,1,6),_CldVirtualTotalPackets_Type())
cldVirtualTotalPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cldVirtualTotalPackets.setStatus(_D)
_CldVirtualTotalBytes_Type=Counter32
_CldVirtualTotalBytes_Object=MibTableColumn
cldVirtualTotalBytes=_CldVirtualTotalBytes_Object((1,3,6,1,4,1,9,9,99,1,1,1,1,7),_CldVirtualTotalBytes_Type())
cldVirtualTotalBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cldVirtualTotalBytes.setStatus(_D)
class _CldVirtualWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CldVirtualWeight_Type.__name__=_G
_CldVirtualWeight_Object=MibTableColumn
cldVirtualWeight=_CldVirtualWeight_Object((1,3,6,1,4,1,9,9,99,1,1,1,1,8),_CldVirtualWeight_Type())
cldVirtualWeight.setMaxAccess(_C)
if mibBuilder.loadTexts:cldVirtualWeight.setStatus(_D)
_CldeVirtualTable_Object=MibTable
cldeVirtualTable=_CldeVirtualTable_Object((1,3,6,1,4,1,9,9,99,1,1,2))
if mibBuilder.loadTexts:cldeVirtualTable.setStatus(_F)
_CldeVirtualTableEntry_Object=MibTableRow
cldeVirtualTableEntry=_CldeVirtualTableEntry_Object((1,3,6,1,4,1,9,9,99,1,1,2,1))
cldeVirtualTableEntry.setIndexNames((0,_A,_b),(0,_A,_c),(0,_A,_d),(0,_A,_e))
if mibBuilder.loadTexts:cldeVirtualTableEntry.setStatus(_F)
_CldeVirtualIpAddress_Type=IpAddress
_CldeVirtualIpAddress_Object=MibTableColumn
cldeVirtualIpAddress=_CldeVirtualIpAddress_Object((1,3,6,1,4,1,9,9,99,1,1,2,1,1),_CldeVirtualIpAddress_Type())
cldeVirtualIpAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:cldeVirtualIpAddress.setStatus(_F)
class _CldeVirtualPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CldeVirtualPort_Type.__name__=_G
_CldeVirtualPort_Object=MibTableColumn
cldeVirtualPort=_CldeVirtualPort_Object((1,3,6,1,4,1,9,9,99,1,1,2,1,2),_CldeVirtualPort_Type())
cldeVirtualPort.setMaxAccess(_E)
if mibBuilder.loadTexts:cldeVirtualPort.setStatus(_F)
class _CldeVirtualBindID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CldeVirtualBindID_Type.__name__=_G
_CldeVirtualBindID_Object=MibTableColumn
cldeVirtualBindID=_CldeVirtualBindID_Object((1,3,6,1,4,1,9,9,99,1,1,2,1,3),_CldeVirtualBindID_Type())
cldeVirtualBindID.setMaxAccess(_E)
if mibBuilder.loadTexts:cldeVirtualBindID.setStatus(_F)
_CldeVirtualProtocol_Type=MachineProtocol
_CldeVirtualProtocol_Object=MibTableColumn
cldeVirtualProtocol=_CldeVirtualProtocol_Object((1,3,6,1,4,1,9,9,99,1,1,2,1,4),_CldeVirtualProtocol_Type())
cldeVirtualProtocol.setMaxAccess(_E)
if mibBuilder.loadTexts:cldeVirtualProtocol.setStatus(_F)
_CldeVirtualState_Type=CldMachineState
_CldeVirtualState_Object=MibTableColumn
cldeVirtualState=_CldeVirtualState_Object((1,3,6,1,4,1,9,9,99,1,1,2,1,5),_CldeVirtualState_Type())
cldeVirtualState.setMaxAccess(_C)
if mibBuilder.loadTexts:cldeVirtualState.setStatus(_F)
_CldeVirtualTotalConnections_Type=Counter32
_CldeVirtualTotalConnections_Object=MibTableColumn
cldeVirtualTotalConnections=_CldeVirtualTotalConnections_Object((1,3,6,1,4,1,9,9,99,1,1,2,1,6),_CldeVirtualTotalConnections_Type())
cldeVirtualTotalConnections.setMaxAccess(_C)
if mibBuilder.loadTexts:cldeVirtualTotalConnections.setStatus(_F)
_CldeVirtualTotalPackets_Type=Counter32
_CldeVirtualTotalPackets_Object=MibTableColumn
cldeVirtualTotalPackets=_CldeVirtualTotalPackets_Object((1,3,6,1,4,1,9,9,99,1,1,2,1,7),_CldeVirtualTotalPackets_Type())
cldeVirtualTotalPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cldeVirtualTotalPackets.setStatus(_F)
_CldeVirtualTotalBytes_Type=Counter32
_CldeVirtualTotalBytes_Object=MibTableColumn
cldeVirtualTotalBytes=_CldeVirtualTotalBytes_Object((1,3,6,1,4,1,9,9,99,1,1,2,1,8),_CldeVirtualTotalBytes_Type())
cldeVirtualTotalBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cldeVirtualTotalBytes.setStatus(_F)
class _CldeVirtualWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CldeVirtualWeight_Type.__name__=_G
_CldeVirtualWeight_Object=MibTableColumn
cldeVirtualWeight=_CldeVirtualWeight_Object((1,3,6,1,4,1,9,9,99,1,1,2,1,9),_CldeVirtualWeight_Type())
cldeVirtualWeight.setMaxAccess(_C)
if mibBuilder.loadTexts:cldeVirtualWeight.setStatus(_F)
_CldexVirtualTable_Object=MibTable
cldexVirtualTable=_CldexVirtualTable_Object((1,3,6,1,4,1,9,9,99,1,1,3))
if mibBuilder.loadTexts:cldexVirtualTable.setStatus(_B)
_CldexVirtualTableEntry_Object=MibTableRow
cldexVirtualTableEntry=_CldexVirtualTableEntry_Object((1,3,6,1,4,1,9,9,99,1,1,3,1))
cldexVirtualTableEntry.setIndexNames((0,_A,_f),(0,_A,_g),(0,_A,_h),(0,_A,_i),(0,_A,_j))
if mibBuilder.loadTexts:cldexVirtualTableEntry.setStatus(_B)
_CldexVirtualIpAddress_Type=IpAddress
_CldexVirtualIpAddress_Object=MibTableColumn
cldexVirtualIpAddress=_CldexVirtualIpAddress_Object((1,3,6,1,4,1,9,9,99,1,1,3,1,1),_CldexVirtualIpAddress_Type())
cldexVirtualIpAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:cldexVirtualIpAddress.setStatus(_B)
class _CldexVirtualPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CldexVirtualPort_Type.__name__=_G
_CldexVirtualPort_Object=MibTableColumn
cldexVirtualPort=_CldexVirtualPort_Object((1,3,6,1,4,1,9,9,99,1,1,3,1,2),_CldexVirtualPort_Type())
cldexVirtualPort.setMaxAccess(_E)
if mibBuilder.loadTexts:cldexVirtualPort.setStatus(_B)
class _CldexVirtualBindID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CldexVirtualBindID_Type.__name__=_G
_CldexVirtualBindID_Object=MibTableColumn
cldexVirtualBindID=_CldexVirtualBindID_Object((1,3,6,1,4,1,9,9,99,1,1,3,1,3),_CldexVirtualBindID_Type())
cldexVirtualBindID.setMaxAccess(_E)
if mibBuilder.loadTexts:cldexVirtualBindID.setStatus(_B)
_CldexVirtualProtocol_Type=MachineProtocol
_CldexVirtualProtocol_Object=MibTableColumn
cldexVirtualProtocol=_CldexVirtualProtocol_Object((1,3,6,1,4,1,9,9,99,1,1,3,1,4),_CldexVirtualProtocol_Type())
cldexVirtualProtocol.setMaxAccess(_E)
if mibBuilder.loadTexts:cldexVirtualProtocol.setStatus(_B)
class _CldexVirtualRule_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_CldexVirtualRule_Type.__name__=_X
_CldexVirtualRule_Object=MibTableColumn
cldexVirtualRule=_CldexVirtualRule_Object((1,3,6,1,4,1,9,9,99,1,1,3,1,5),_CldexVirtualRule_Type())
cldexVirtualRule.setMaxAccess(_E)
if mibBuilder.loadTexts:cldexVirtualRule.setStatus(_B)
_CldexVirtualState_Type=CldMachineState
_CldexVirtualState_Object=MibTableColumn
cldexVirtualState=_CldexVirtualState_Object((1,3,6,1,4,1,9,9,99,1,1,3,1,6),_CldexVirtualState_Type())
cldexVirtualState.setMaxAccess(_C)
if mibBuilder.loadTexts:cldexVirtualState.setStatus(_B)
_CldexVirtualTotalConnections_Type=Counter32
_CldexVirtualTotalConnections_Object=MibTableColumn
cldexVirtualTotalConnections=_CldexVirtualTotalConnections_Object((1,3,6,1,4,1,9,9,99,1,1,3,1,7),_CldexVirtualTotalConnections_Type())
cldexVirtualTotalConnections.setMaxAccess(_C)
if mibBuilder.loadTexts:cldexVirtualTotalConnections.setStatus(_B)
_CldexVirtualTotalPackets_Type=Counter32
_CldexVirtualTotalPackets_Object=MibTableColumn
cldexVirtualTotalPackets=_CldexVirtualTotalPackets_Object((1,3,6,1,4,1,9,9,99,1,1,3,1,8),_CldexVirtualTotalPackets_Type())
cldexVirtualTotalPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cldexVirtualTotalPackets.setStatus(_B)
_CldexVirtualTotalBytes_Type=Counter32
_CldexVirtualTotalBytes_Object=MibTableColumn
cldexVirtualTotalBytes=_CldexVirtualTotalBytes_Object((1,3,6,1,4,1,9,9,99,1,1,3,1,9),_CldexVirtualTotalBytes_Type())
cldexVirtualTotalBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cldexVirtualTotalBytes.setStatus(_B)
class _CldexVirtualWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CldexVirtualWeight_Type.__name__=_G
_CldexVirtualWeight_Object=MibTableColumn
cldexVirtualWeight=_CldexVirtualWeight_Object((1,3,6,1,4,1,9,9,99,1,1,3,1,10),_CldexVirtualWeight_Type())
cldexVirtualWeight.setMaxAccess(_C)
if mibBuilder.loadTexts:cldexVirtualWeight.setStatus(_B)
_CldRealMachine_ObjectIdentity=ObjectIdentity
cldRealMachine=_CldRealMachine_ObjectIdentity((1,3,6,1,4,1,9,9,99,1,2))
_CldRealTable_Object=MibTable
cldRealTable=_CldRealTable_Object((1,3,6,1,4,1,9,9,99,1,2,1))
if mibBuilder.loadTexts:cldRealTable.setStatus(_D)
_CldRealTableEntry_Object=MibTableRow
cldRealTableEntry=_CldRealTableEntry_Object((1,3,6,1,4,1,9,9,99,1,2,1,1))
cldRealTableEntry.setIndexNames((0,_A,_k),(0,_A,_l))
if mibBuilder.loadTexts:cldRealTableEntry.setStatus(_D)
_CldRealIpAddress_Type=IpAddress
_CldRealIpAddress_Object=MibTableColumn
cldRealIpAddress=_CldRealIpAddress_Object((1,3,6,1,4,1,9,9,99,1,2,1,1,1),_CldRealIpAddress_Type())
cldRealIpAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:cldRealIpAddress.setStatus(_D)
class _CldRealPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CldRealPort_Type.__name__=_G
_CldRealPort_Object=MibTableColumn
cldRealPort=_CldRealPort_Object((1,3,6,1,4,1,9,9,99,1,2,1,1,2),_CldRealPort_Type())
cldRealPort.setMaxAccess(_E)
if mibBuilder.loadTexts:cldRealPort.setStatus(_D)
_CldRealState_Type=CldMachineState
_CldRealState_Object=MibTableColumn
cldRealState=_CldRealState_Object((1,3,6,1,4,1,9,9,99,1,2,1,1,3),_CldRealState_Type())
cldRealState.setMaxAccess(_C)
if mibBuilder.loadTexts:cldRealState.setStatus(_D)
_CldRealTotalConnections_Type=Counter32
_CldRealTotalConnections_Object=MibTableColumn
cldRealTotalConnections=_CldRealTotalConnections_Object((1,3,6,1,4,1,9,9,99,1,2,1,1,4),_CldRealTotalConnections_Type())
cldRealTotalConnections.setMaxAccess(_C)
if mibBuilder.loadTexts:cldRealTotalConnections.setStatus(_D)
_CldRealTotalPackets_Type=Counter32
_CldRealTotalPackets_Object=MibTableColumn
cldRealTotalPackets=_CldRealTotalPackets_Object((1,3,6,1,4,1,9,9,99,1,2,1,1,5),_CldRealTotalPackets_Type())
cldRealTotalPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cldRealTotalPackets.setStatus(_D)
_CldRealTotalBytes_Type=Counter32
_CldRealTotalBytes_Object=MibTableColumn
cldRealTotalBytes=_CldRealTotalBytes_Object((1,3,6,1,4,1,9,9,99,1,2,1,1,6),_CldRealTotalBytes_Type())
cldRealTotalBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cldRealTotalBytes.setStatus(_D)
class _CldRealWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CldRealWeight_Type.__name__=_G
_CldRealWeight_Object=MibTableColumn
cldRealWeight=_CldRealWeight_Object((1,3,6,1,4,1,9,9,99,1,2,1,1,7),_CldRealWeight_Type())
cldRealWeight.setMaxAccess(_m)
if mibBuilder.loadTexts:cldRealWeight.setStatus(_D)
_CldeRealTable_Object=MibTable
cldeRealTable=_CldeRealTable_Object((1,3,6,1,4,1,9,9,99,1,2,2))
if mibBuilder.loadTexts:cldeRealTable.setStatus(_B)
_CldeRealTableEntry_Object=MibTableRow
cldeRealTableEntry=_CldeRealTableEntry_Object((1,3,6,1,4,1,9,9,99,1,2,2,1))
cldeRealTableEntry.setIndexNames((0,_A,_n),(0,_A,_o),(0,_A,_p),(0,_A,_q))
if mibBuilder.loadTexts:cldeRealTableEntry.setStatus(_B)
_CldeRealIpAddress_Type=IpAddress
_CldeRealIpAddress_Object=MibTableColumn
cldeRealIpAddress=_CldeRealIpAddress_Object((1,3,6,1,4,1,9,9,99,1,2,2,1,1),_CldeRealIpAddress_Type())
cldeRealIpAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:cldeRealIpAddress.setStatus(_B)
class _CldeRealPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CldeRealPort_Type.__name__=_G
_CldeRealPort_Object=MibTableColumn
cldeRealPort=_CldeRealPort_Object((1,3,6,1,4,1,9,9,99,1,2,2,1,2),_CldeRealPort_Type())
cldeRealPort.setMaxAccess(_E)
if mibBuilder.loadTexts:cldeRealPort.setStatus(_B)
_CldeRealBindID_Type=MachineBindID
_CldeRealBindID_Object=MibTableColumn
cldeRealBindID=_CldeRealBindID_Object((1,3,6,1,4,1,9,9,99,1,2,2,1,3),_CldeRealBindID_Type())
cldeRealBindID.setMaxAccess(_E)
if mibBuilder.loadTexts:cldeRealBindID.setStatus(_B)
_CldeRealProtocol_Type=MachineProtocol
_CldeRealProtocol_Object=MibTableColumn
cldeRealProtocol=_CldeRealProtocol_Object((1,3,6,1,4,1,9,9,99,1,2,2,1,4),_CldeRealProtocol_Type())
cldeRealProtocol.setMaxAccess(_E)
if mibBuilder.loadTexts:cldeRealProtocol.setStatus(_B)
_CldeRealState_Type=CldMachineState
_CldeRealState_Object=MibTableColumn
cldeRealState=_CldeRealState_Object((1,3,6,1,4,1,9,9,99,1,2,2,1,5),_CldeRealState_Type())
cldeRealState.setMaxAccess(_C)
if mibBuilder.loadTexts:cldeRealState.setStatus(_B)
_CldeRealTotalConnections_Type=Counter32
_CldeRealTotalConnections_Object=MibTableColumn
cldeRealTotalConnections=_CldeRealTotalConnections_Object((1,3,6,1,4,1,9,9,99,1,2,2,1,6),_CldeRealTotalConnections_Type())
cldeRealTotalConnections.setMaxAccess(_C)
if mibBuilder.loadTexts:cldeRealTotalConnections.setStatus(_B)
_CldeRealTotalPackets_Type=Counter32
_CldeRealTotalPackets_Object=MibTableColumn
cldeRealTotalPackets=_CldeRealTotalPackets_Object((1,3,6,1,4,1,9,9,99,1,2,2,1,7),_CldeRealTotalPackets_Type())
cldeRealTotalPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cldeRealTotalPackets.setStatus(_B)
_CldeRealTotalBytes_Type=Counter32
_CldeRealTotalBytes_Object=MibTableColumn
cldeRealTotalBytes=_CldeRealTotalBytes_Object((1,3,6,1,4,1,9,9,99,1,2,2,1,8),_CldeRealTotalBytes_Type())
cldeRealTotalBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cldeRealTotalBytes.setStatus(_B)
class _CldeRealWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CldeRealWeight_Type.__name__=_G
_CldeRealWeight_Object=MibTableColumn
cldeRealWeight=_CldeRealWeight_Object((1,3,6,1,4,1,9,9,99,1,2,2,1,9),_CldeRealWeight_Type())
cldeRealWeight.setMaxAccess(_m)
if mibBuilder.loadTexts:cldeRealWeight.setStatus(_B)
_CldFailover_ObjectIdentity=ObjectIdentity
cldFailover=_CldFailover_ObjectIdentity((1,3,6,1,4,1,9,9,99,1,3))
_CldFailoverEnabled_Type=CldFailoverEnabledState
_CldFailoverEnabled_Object=MibScalar
cldFailoverEnabled=_CldFailoverEnabled_Object((1,3,6,1,4,1,9,9,99,1,3,1),_CldFailoverEnabled_Type())
cldFailoverEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cldFailoverEnabled.setStatus(_B)
_CldFailoverCableStatus_Type=CldFailoverCableState
_CldFailoverCableStatus_Object=MibScalar
cldFailoverCableStatus=_CldFailoverCableStatus_Object((1,3,6,1,4,1,9,9,99,1,3,2),_CldFailoverCableStatus_Type())
cldFailoverCableStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cldFailoverCableStatus.setStatus(_B)
_CldFailoverUnitType_Type=CldFailoverUnitTypeDescriptor
_CldFailoverUnitType_Object=MibScalar
cldFailoverUnitType=_CldFailoverUnitType_Object((1,3,6,1,4,1,9,9,99,1,3,3),_CldFailoverUnitType_Type())
cldFailoverUnitType.setMaxAccess(_C)
if mibBuilder.loadTexts:cldFailoverUnitType.setStatus(_B)
_CldFailoverUnitStatus_Type=CldFailoverUnitStatusDescriptor
_CldFailoverUnitStatus_Object=MibScalar
cldFailoverUnitStatus=_CldFailoverUnitStatus_Object((1,3,6,1,4,1,9,9,99,1,3,4),_CldFailoverUnitStatus_Type())
cldFailoverUnitStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cldFailoverUnitStatus.setStatus(_B)
_CldFailoverActiveTimeStamp_Type=TimeStamp
_CldFailoverActiveTimeStamp_Object=MibScalar
cldFailoverActiveTimeStamp=_CldFailoverActiveTimeStamp_Object((1,3,6,1,4,1,9,9,99,1,3,5),_CldFailoverActiveTimeStamp_Type())
cldFailoverActiveTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:cldFailoverActiveTimeStamp.setStatus(_B)
_CiscoLocalDirectorMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
ciscoLocalDirectorMIBNotificationPrefix=_CiscoLocalDirectorMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,99,2))
_CiscoLocalDirectorMIBNotifications_ObjectIdentity=ObjectIdentity
ciscoLocalDirectorMIBNotifications=_CiscoLocalDirectorMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,99,2,0))
_CiscoLocalDirectorMIBConformance_ObjectIdentity=ObjectIdentity
ciscoLocalDirectorMIBConformance=_CiscoLocalDirectorMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,99,3))
_CiscoLocalDirectorMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoLocalDirectorMIBCompliances=_CiscoLocalDirectorMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,99,3,1))
_CiscoLocalDirectorMIBGroups_ObjectIdentity=ObjectIdentity
ciscoLocalDirectorMIBGroups=_CiscoLocalDirectorMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,99,3,2))
ciscoLocalDirectorMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,99,3,2,1))
ciscoLocalDirectorMIBGroup.setObjects(*((_A,_K),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_L),(_A,_v),(_A,_w),(_A,_x),(_A,_y)))
if mibBuilder.loadTexts:ciscoLocalDirectorMIBGroup.setStatus(_D)
ciscoLocalDirectorFailoverGroup=ObjectGroup((1,3,6,1,4,1,9,9,99,3,2,2))
ciscoLocalDirectorFailoverGroup.setObjects(*((_A,_M),(_A,_N),(_A,_z),(_A,_O),(_A,_A0)))
if mibBuilder.loadTexts:ciscoLocalDirectorFailoverGroup.setStatus(_B)
ciscoLocalDirectorEMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,99,3,2,3))
ciscoLocalDirectorEMIBGroup.setObjects(*((_A,_P),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_H),(_A,_Q),(_A,_R),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:ciscoLocalDirectorEMIBGroup.setStatus(_F)
ciscoLocalDirectorEMIBGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,99,3,2,6))
ciscoLocalDirectorEMIBGroupRev1.setObjects(*((_A,_U),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_H),(_A,_Q),(_A,_R),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:ciscoLocalDirectorEMIBGroupRev1.setStatus(_B)
ciscoLocalDirectorVirtualStateChange=NotificationType((1,3,6,1,4,1,9,9,99,2,0,1))
ciscoLocalDirectorVirtualStateChange.setObjects((_A,_K))
if mibBuilder.loadTexts:ciscoLocalDirectorVirtualStateChange.setStatus(_D)
ciscoLocalDirectorRealStateChange=NotificationType((1,3,6,1,4,1,9,9,99,2,0,2))
ciscoLocalDirectorRealStateChange.setObjects((_A,_L))
if mibBuilder.loadTexts:ciscoLocalDirectorRealStateChange.setStatus(_D)
ciscoLocalDirectorFailoverEnableChange=NotificationType((1,3,6,1,4,1,9,9,99,2,0,3))
ciscoLocalDirectorFailoverEnableChange.setObjects((_A,_M))
if mibBuilder.loadTexts:ciscoLocalDirectorFailoverEnableChange.setStatus(_B)
ciscoLocalDirectorFailoverCableChange=NotificationType((1,3,6,1,4,1,9,9,99,2,0,4))
ciscoLocalDirectorFailoverCableChange.setObjects((_A,_N))
if mibBuilder.loadTexts:ciscoLocalDirectorFailoverCableChange.setStatus(_B)
ciscoLocalDirectorFailoverUnitStatus=NotificationType((1,3,6,1,4,1,9,9,99,2,0,5))
ciscoLocalDirectorFailoverUnitStatus.setObjects((_A,_O))
if mibBuilder.loadTexts:ciscoLocalDirectorFailoverUnitStatus.setStatus(_B)
ciscoLocalDirectorEVirtualStateChange=NotificationType((1,3,6,1,4,1,9,9,99,2,0,6))
ciscoLocalDirectorEVirtualStateChange.setObjects((_A,_P))
if mibBuilder.loadTexts:ciscoLocalDirectorEVirtualStateChange.setStatus(_F)
ciscoLocalDirectorERealStateChange=NotificationType((1,3,6,1,4,1,9,9,99,2,0,7))
ciscoLocalDirectorERealStateChange.setObjects((_A,_H))
if mibBuilder.loadTexts:ciscoLocalDirectorERealStateChange.setStatus(_B)
ciscoLocalDirectorExVirtualStateChange=NotificationType((1,3,6,1,4,1,9,9,99,2,0,8))
ciscoLocalDirectorExVirtualStateChange.setObjects((_A,_U))
if mibBuilder.loadTexts:ciscoLocalDirectorExVirtualStateChange.setStatus(_B)
ciscoLocalDirectorNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,99,3,2,4))
ciscoLocalDirectorNotificationGroup.setObjects(*((_A,_A9),(_A,_AA),(_A,_I),(_A,_J),(_A,_V)))
if mibBuilder.loadTexts:ciscoLocalDirectorNotificationGroup.setStatus(_D)
ciscoLocalDirectorNotificationGroupRev1=NotificationGroup((1,3,6,1,4,1,9,9,99,3,2,5))
ciscoLocalDirectorNotificationGroupRev1.setObjects(*((_A,_AB),(_A,_W),(_A,_I),(_A,_J),(_A,_V)))
if mibBuilder.loadTexts:ciscoLocalDirectorNotificationGroupRev1.setStatus(_F)
ciscoLocalDirectorNotificationGroupRev2=NotificationGroup((1,3,6,1,4,1,9,9,99,3,2,7))
ciscoLocalDirectorNotificationGroupRev2.setObjects(*((_A,_AC),(_A,_W),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:ciscoLocalDirectorNotificationGroupRev2.setStatus(_B)
ciscoLocalDirectorMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,99,3,1,1))
ciscoLocalDirectorMIBCompliance.setObjects((_A,_AD))
if mibBuilder.loadTexts:ciscoLocalDirectorMIBCompliance.setStatus(_F)
mibBuilder.exportSymbols(_A,**{'CldMachineState':CldMachineState,'CldFailoverEnabledState':CldFailoverEnabledState,'CldFailoverCableState':CldFailoverCableState,'CldFailoverUnitTypeDescriptor':CldFailoverUnitTypeDescriptor,'CldFailoverUnitStatusDescriptor':CldFailoverUnitStatusDescriptor,'MachineProtocol':MachineProtocol,'MachineBindID':MachineBindID,'ciscoLocalDirectorMIB':ciscoLocalDirectorMIB,'ciscoLocalDirectorMIBObjects':ciscoLocalDirectorMIBObjects,'cldVirtualMachine':cldVirtualMachine,'cldVirtualTable':cldVirtualTable,'cldVirtualTableEntry':cldVirtualTableEntry,_Y:cldVirtualIpAddress,_Z:cldVirtualPort,_a:cldVirtualBindID,_K:cldVirtualState,_r:cldVirtualTotalConnections,_s:cldVirtualTotalPackets,_t:cldVirtualTotalBytes,_u:cldVirtualWeight,'cldeVirtualTable':cldeVirtualTable,'cldeVirtualTableEntry':cldeVirtualTableEntry,_b:cldeVirtualIpAddress,_c:cldeVirtualPort,_d:cldeVirtualBindID,_e:cldeVirtualProtocol,_P:cldeVirtualState,_A1:cldeVirtualTotalConnections,_A2:cldeVirtualTotalPackets,_A3:cldeVirtualTotalBytes,_A4:cldeVirtualWeight,'cldexVirtualTable':cldexVirtualTable,'cldexVirtualTableEntry':cldexVirtualTableEntry,_f:cldexVirtualIpAddress,_g:cldexVirtualPort,_h:cldexVirtualBindID,_i:cldexVirtualProtocol,_j:cldexVirtualRule,_U:cldexVirtualState,_A5:cldexVirtualTotalConnections,_A6:cldexVirtualTotalPackets,_A7:cldexVirtualTotalBytes,_A8:cldexVirtualWeight,'cldRealMachine':cldRealMachine,'cldRealTable':cldRealTable,'cldRealTableEntry':cldRealTableEntry,_k:cldRealIpAddress,_l:cldRealPort,_L:cldRealState,_v:cldRealTotalConnections,_w:cldRealTotalPackets,_x:cldRealTotalBytes,_y:cldRealWeight,'cldeRealTable':cldeRealTable,'cldeRealTableEntry':cldeRealTableEntry,_n:cldeRealIpAddress,_o:cldeRealPort,_p:cldeRealBindID,_q:cldeRealProtocol,_H:cldeRealState,_Q:cldeRealTotalConnections,_R:cldeRealTotalPackets,_S:cldeRealTotalBytes,_T:cldeRealWeight,'cldFailover':cldFailover,_M:cldFailoverEnabled,_N:cldFailoverCableStatus,_z:cldFailoverUnitType,_O:cldFailoverUnitStatus,_A0:cldFailoverActiveTimeStamp,'ciscoLocalDirectorMIBNotificationPrefix':ciscoLocalDirectorMIBNotificationPrefix,'ciscoLocalDirectorMIBNotifications':ciscoLocalDirectorMIBNotifications,_A9:ciscoLocalDirectorVirtualStateChange,_AA:ciscoLocalDirectorRealStateChange,_I:ciscoLocalDirectorFailoverEnableChange,_J:ciscoLocalDirectorFailoverCableChange,_V:ciscoLocalDirectorFailoverUnitStatus,_AB:ciscoLocalDirectorEVirtualStateChange,_W:ciscoLocalDirectorERealStateChange,_AC:ciscoLocalDirectorExVirtualStateChange,'ciscoLocalDirectorMIBConformance':ciscoLocalDirectorMIBConformance,'ciscoLocalDirectorMIBCompliances':ciscoLocalDirectorMIBCompliances,'ciscoLocalDirectorMIBCompliance':ciscoLocalDirectorMIBCompliance,'ciscoLocalDirectorMIBGroups':ciscoLocalDirectorMIBGroups,'ciscoLocalDirectorMIBGroup':ciscoLocalDirectorMIBGroup,_AD:ciscoLocalDirectorFailoverGroup,'ciscoLocalDirectorEMIBGroup':ciscoLocalDirectorEMIBGroup,'ciscoLocalDirectorNotificationGroup':ciscoLocalDirectorNotificationGroup,'ciscoLocalDirectorNotificationGroupRev1':ciscoLocalDirectorNotificationGroupRev1,'ciscoLocalDirectorEMIBGroupRev1':ciscoLocalDirectorEMIBGroupRev1,'ciscoLocalDirectorNotificationGroupRev2':ciscoLocalDirectorNotificationGroupRev2})