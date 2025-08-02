_H='Integer32'
_G='read-only'
_F='dsMgcpSlotIndex'
_E='DASAN-ACCESS-SLOT-MGCP-MIB'
_D='1.1.1.1'
_C='DisplayString'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dasanMgmt,=mibBuilder.importSymbols('DASAN-SMI','dasanMgmt')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
AutonomousType,DisplayString,PhysAddress,RowStatus,TextualConvention,TestAndIncr,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','AutonomousType',_C,'PhysAddress','RowStatus','TextualConvention','TestAndIncr','TimeStamp')
dasanAccessMib=ModuleIdentity((1,3,6,1,4,1,6296,9,100))
if mibBuilder.loadTexts:dasanAccessMib.setRevisions(('2005-02-11 21:00',))
_DasanAccGatewayMIBObjects_ObjectIdentity=ObjectIdentity
dasanAccGatewayMIBObjects=_DasanAccGatewayMIBObjects_ObjectIdentity((1,3,6,1,4,1,6296,9,100,2))
_DsAccGwyMgcp_ObjectIdentity=ObjectIdentity
dsAccGwyMgcp=_DsAccGwyMgcp_ObjectIdentity((1,3,6,1,4,1,6296,9,100,2,2))
_DsAccGwyMgcpConfiguration_ObjectIdentity=ObjectIdentity
dsAccGwyMgcpConfiguration=_DsAccGwyMgcpConfiguration_ObjectIdentity((1,3,6,1,4,1,6296,9,100,2,2,1))
_DsAccGwyConfigMgcpSlot_ObjectIdentity=ObjectIdentity
dsAccGwyConfigMgcpSlot=_DsAccGwyConfigMgcpSlot_ObjectIdentity((1,3,6,1,4,1,6296,9,100,2,2,1,1))
_DsAccGwyConfigMgcpSlotTable_Object=MibTable
dsAccGwyConfigMgcpSlotTable=_DsAccGwyConfigMgcpSlotTable_Object((1,3,6,1,4,1,6296,9,100,2,2,1,1,1))
if mibBuilder.loadTexts:dsAccGwyConfigMgcpSlotTable.setStatus(_A)
_DsAccGwyConfigMgcpSlotEntry_Object=MibTableRow
dsAccGwyConfigMgcpSlotEntry=_DsAccGwyConfigMgcpSlotEntry_Object((1,3,6,1,4,1,6296,9,100,2,2,1,1,1,1))
dsAccGwyConfigMgcpSlotEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:dsAccGwyConfigMgcpSlotEntry.setStatus(_A)
_DsMgcpSlotIndex_Type=Integer32
_DsMgcpSlotIndex_Object=MibTableColumn
dsMgcpSlotIndex=_DsMgcpSlotIndex_Object((1,3,6,1,4,1,6296,9,100,2,2,1,1,1,1,1),_DsMgcpSlotIndex_Type())
dsMgcpSlotIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:dsMgcpSlotIndex.setStatus(_A)
class _DsMgcpSlotEncodePackageName_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('off',0),('on',1)))
_DsMgcpSlotEncodePackageName_Type.__name__=_H
_DsMgcpSlotEncodePackageName_Object=MibTableColumn
dsMgcpSlotEncodePackageName=_DsMgcpSlotEncodePackageName_Object((1,3,6,1,4,1,6296,9,100,2,2,1,1,1,1,2),_DsMgcpSlotEncodePackageName_Type())
dsMgcpSlotEncodePackageName.setMaxAccess(_B)
if mibBuilder.loadTexts:dsMgcpSlotEncodePackageName.setStatus(_A)
_DsMgcpSlotRetransmitStartTimeout_Type=Integer32
_DsMgcpSlotRetransmitStartTimeout_Object=MibTableColumn
dsMgcpSlotRetransmitStartTimeout=_DsMgcpSlotRetransmitStartTimeout_Object((1,3,6,1,4,1,6296,9,100,2,2,1,1,1,1,3),_DsMgcpSlotRetransmitStartTimeout_Type())
dsMgcpSlotRetransmitStartTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:dsMgcpSlotRetransmitStartTimeout.setStatus(_A)
_DsMgcpSlotRetransmitMaxTimeout_Type=Integer32
_DsMgcpSlotRetransmitMaxTimeout_Object=MibTableColumn
dsMgcpSlotRetransmitMaxTimeout=_DsMgcpSlotRetransmitMaxTimeout_Object((1,3,6,1,4,1,6296,9,100,2,2,1,1,1,1,4),_DsMgcpSlotRetransmitMaxTimeout_Type())
dsMgcpSlotRetransmitMaxTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:dsMgcpSlotRetransmitMaxTimeout.setStatus(_A)
_DsMgcpSlotRetransmitLongTimer_Type=Integer32
_DsMgcpSlotRetransmitLongTimer_Object=MibTableColumn
dsMgcpSlotRetransmitLongTimer=_DsMgcpSlotRetransmitLongTimer_Object((1,3,6,1,4,1,6296,9,100,2,2,1,1,1,1,5),_DsMgcpSlotRetransmitLongTimer_Type())
dsMgcpSlotRetransmitLongTimer.setMaxAccess(_G)
if mibBuilder.loadTexts:dsMgcpSlotRetransmitLongTimer.setStatus(_A)
_DsMgcpSlotRetransmitMaxLifetime_Type=Integer32
_DsMgcpSlotRetransmitMaxLifetime_Object=MibTableColumn
dsMgcpSlotRetransmitMaxLifetime=_DsMgcpSlotRetransmitMaxLifetime_Object((1,3,6,1,4,1,6296,9,100,2,2,1,1,1,1,6),_DsMgcpSlotRetransmitMaxLifetime_Type())
dsMgcpSlotRetransmitMaxLifetime.setMaxAccess(_B)
if mibBuilder.loadTexts:dsMgcpSlotRetransmitMaxLifetime.setStatus(_A)
_DsMgcpSlotRetransmitMax1_Type=Integer32
_DsMgcpSlotRetransmitMax1_Object=MibTableColumn
dsMgcpSlotRetransmitMax1=_DsMgcpSlotRetransmitMax1_Object((1,3,6,1,4,1,6296,9,100,2,2,1,1,1,1,7),_DsMgcpSlotRetransmitMax1_Type())
dsMgcpSlotRetransmitMax1.setMaxAccess(_B)
if mibBuilder.loadTexts:dsMgcpSlotRetransmitMax1.setStatus(_A)
_DsMgcpSlotRetransmitMax2_Type=Integer32
_DsMgcpSlotRetransmitMax2_Object=MibTableColumn
dsMgcpSlotRetransmitMax2=_DsMgcpSlotRetransmitMax2_Object((1,3,6,1,4,1,6296,9,100,2,2,1,1,1,1,8),_DsMgcpSlotRetransmitMax2_Type())
dsMgcpSlotRetransmitMax2.setMaxAccess(_B)
if mibBuilder.loadTexts:dsMgcpSlotRetransmitMax2.setStatus(_A)
_DsMgcpSlotRestartMaxwait_Type=Integer32
_DsMgcpSlotRestartMaxwait_Object=MibTableColumn
dsMgcpSlotRestartMaxwait=_DsMgcpSlotRestartMaxwait_Object((1,3,6,1,4,1,6296,9,100,2,2,1,1,1,1,9),_DsMgcpSlotRestartMaxwait_Type())
dsMgcpSlotRestartMaxwait.setMaxAccess(_B)
if mibBuilder.loadTexts:dsMgcpSlotRestartMaxwait.setStatus(_A)
_DsMgcpSlotDisconnectInit_Type=Integer32
_DsMgcpSlotDisconnectInit_Object=MibTableColumn
dsMgcpSlotDisconnectInit=_DsMgcpSlotDisconnectInit_Object((1,3,6,1,4,1,6296,9,100,2,2,1,1,1,1,10),_DsMgcpSlotDisconnectInit_Type())
dsMgcpSlotDisconnectInit.setMaxAccess(_B)
if mibBuilder.loadTexts:dsMgcpSlotDisconnectInit.setStatus(_A)
_DsMgcpSlotDisconnectMin_Type=Integer32
_DsMgcpSlotDisconnectMin_Object=MibTableColumn
dsMgcpSlotDisconnectMin=_DsMgcpSlotDisconnectMin_Object((1,3,6,1,4,1,6296,9,100,2,2,1,1,1,1,11),_DsMgcpSlotDisconnectMin_Type())
dsMgcpSlotDisconnectMin.setMaxAccess(_B)
if mibBuilder.loadTexts:dsMgcpSlotDisconnectMin.setStatus(_A)
_DsMgcpSlotDisconnectMax_Type=Integer32
_DsMgcpSlotDisconnectMax_Object=MibTableColumn
dsMgcpSlotDisconnectMax=_DsMgcpSlotDisconnectMax_Object((1,3,6,1,4,1,6296,9,100,2,2,1,1,1,1,12),_DsMgcpSlotDisconnectMax_Type())
dsMgcpSlotDisconnectMax.setMaxAccess(_B)
if mibBuilder.loadTexts:dsMgcpSlotDisconnectMax.setStatus(_A)
class _DsMgcpSlotCaAddr1_Type(DisplayString):defaultValue=OctetString(_D)
_DsMgcpSlotCaAddr1_Type.__name__=_C
_DsMgcpSlotCaAddr1_Object=MibTableColumn
dsMgcpSlotCaAddr1=_DsMgcpSlotCaAddr1_Object((1,3,6,1,4,1,6296,9,100,2,2,1,1,1,1,13),_DsMgcpSlotCaAddr1_Type())
dsMgcpSlotCaAddr1.setMaxAccess(_B)
if mibBuilder.loadTexts:dsMgcpSlotCaAddr1.setStatus(_A)
class _DsMgcpSlotCaAddr2_Type(DisplayString):defaultValue=OctetString(_D)
_DsMgcpSlotCaAddr2_Type.__name__=_C
_DsMgcpSlotCaAddr2_Object=MibTableColumn
dsMgcpSlotCaAddr2=_DsMgcpSlotCaAddr2_Object((1,3,6,1,4,1,6296,9,100,2,2,1,1,1,1,14),_DsMgcpSlotCaAddr2_Type())
dsMgcpSlotCaAddr2.setMaxAccess(_B)
if mibBuilder.loadTexts:dsMgcpSlotCaAddr2.setStatus(_A)
class _DsMgcpSlotCaAddr3_Type(DisplayString):defaultValue=OctetString(_D)
_DsMgcpSlotCaAddr3_Type.__name__=_C
_DsMgcpSlotCaAddr3_Object=MibTableColumn
dsMgcpSlotCaAddr3=_DsMgcpSlotCaAddr3_Object((1,3,6,1,4,1,6296,9,100,2,2,1,1,1,1,15),_DsMgcpSlotCaAddr3_Type())
dsMgcpSlotCaAddr3.setMaxAccess(_B)
if mibBuilder.loadTexts:dsMgcpSlotCaAddr3.setStatus(_A)
class _DsMgcpSlotCaAddr4_Type(DisplayString):defaultValue=OctetString(_D)
_DsMgcpSlotCaAddr4_Type.__name__=_C
_DsMgcpSlotCaAddr4_Object=MibTableColumn
dsMgcpSlotCaAddr4=_DsMgcpSlotCaAddr4_Object((1,3,6,1,4,1,6296,9,100,2,2,1,1,1,1,16),_DsMgcpSlotCaAddr4_Type())
dsMgcpSlotCaAddr4.setMaxAccess(_B)
if mibBuilder.loadTexts:dsMgcpSlotCaAddr4.setStatus(_A)
class _DsMgcpSlotCaAddr5_Type(DisplayString):defaultValue=OctetString(_D)
_DsMgcpSlotCaAddr5_Type.__name__=_C
_DsMgcpSlotCaAddr5_Object=MibTableColumn
dsMgcpSlotCaAddr5=_DsMgcpSlotCaAddr5_Object((1,3,6,1,4,1,6296,9,100,2,2,1,1,1,1,17),_DsMgcpSlotCaAddr5_Type())
dsMgcpSlotCaAddr5.setMaxAccess(_B)
if mibBuilder.loadTexts:dsMgcpSlotCaAddr5.setStatus(_A)
class _DsMgcpSlotCaAddr6_Type(DisplayString):defaultValue=OctetString(_D)
_DsMgcpSlotCaAddr6_Type.__name__=_C
_DsMgcpSlotCaAddr6_Object=MibTableColumn
dsMgcpSlotCaAddr6=_DsMgcpSlotCaAddr6_Object((1,3,6,1,4,1,6296,9,100,2,2,1,1,1,1,18),_DsMgcpSlotCaAddr6_Type())
dsMgcpSlotCaAddr6.setMaxAccess(_B)
if mibBuilder.loadTexts:dsMgcpSlotCaAddr6.setStatus(_A)
class _DsMgcpSlotCaAddr7_Type(DisplayString):defaultValue=OctetString(_D)
_DsMgcpSlotCaAddr7_Type.__name__=_C
_DsMgcpSlotCaAddr7_Object=MibTableColumn
dsMgcpSlotCaAddr7=_DsMgcpSlotCaAddr7_Object((1,3,6,1,4,1,6296,9,100,2,2,1,1,1,1,19),_DsMgcpSlotCaAddr7_Type())
dsMgcpSlotCaAddr7.setMaxAccess(_B)
if mibBuilder.loadTexts:dsMgcpSlotCaAddr7.setStatus(_A)
class _DsMgcpSlotCaAddr8_Type(DisplayString):defaultValue=OctetString(_D)
_DsMgcpSlotCaAddr8_Type.__name__=_C
_DsMgcpSlotCaAddr8_Object=MibTableColumn
dsMgcpSlotCaAddr8=_DsMgcpSlotCaAddr8_Object((1,3,6,1,4,1,6296,9,100,2,2,1,1,1,1,20),_DsMgcpSlotCaAddr8_Type())
dsMgcpSlotCaAddr8.setMaxAccess(_B)
if mibBuilder.loadTexts:dsMgcpSlotCaAddr8.setStatus(_A)
_DsMgcpSlotCaPort1_Type=Integer32
_DsMgcpSlotCaPort1_Object=MibTableColumn
dsMgcpSlotCaPort1=_DsMgcpSlotCaPort1_Object((1,3,6,1,4,1,6296,9,100,2,2,1,1,1,1,21),_DsMgcpSlotCaPort1_Type())
dsMgcpSlotCaPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:dsMgcpSlotCaPort1.setStatus(_A)
_DsMgcpSlotCaPort2_Type=Integer32
_DsMgcpSlotCaPort2_Object=MibTableColumn
dsMgcpSlotCaPort2=_DsMgcpSlotCaPort2_Object((1,3,6,1,4,1,6296,9,100,2,2,1,1,1,1,22),_DsMgcpSlotCaPort2_Type())
dsMgcpSlotCaPort2.setMaxAccess(_B)
if mibBuilder.loadTexts:dsMgcpSlotCaPort2.setStatus(_A)
_DsMgcpSlotCaPort3_Type=Integer32
_DsMgcpSlotCaPort3_Object=MibTableColumn
dsMgcpSlotCaPort3=_DsMgcpSlotCaPort3_Object((1,3,6,1,4,1,6296,9,100,2,2,1,1,1,1,23),_DsMgcpSlotCaPort3_Type())
dsMgcpSlotCaPort3.setMaxAccess(_B)
if mibBuilder.loadTexts:dsMgcpSlotCaPort3.setStatus(_A)
_DsMgcpSlotCaPort4_Type=Integer32
_DsMgcpSlotCaPort4_Object=MibTableColumn
dsMgcpSlotCaPort4=_DsMgcpSlotCaPort4_Object((1,3,6,1,4,1,6296,9,100,2,2,1,1,1,1,24),_DsMgcpSlotCaPort4_Type())
dsMgcpSlotCaPort4.setMaxAccess(_B)
if mibBuilder.loadTexts:dsMgcpSlotCaPort4.setStatus(_A)
_DsMgcpSlotCaPort5_Type=Integer32
_DsMgcpSlotCaPort5_Object=MibTableColumn
dsMgcpSlotCaPort5=_DsMgcpSlotCaPort5_Object((1,3,6,1,4,1,6296,9,100,2,2,1,1,1,1,25),_DsMgcpSlotCaPort5_Type())
dsMgcpSlotCaPort5.setMaxAccess(_B)
if mibBuilder.loadTexts:dsMgcpSlotCaPort5.setStatus(_A)
_DsMgcpSlotCaPort6_Type=Integer32
_DsMgcpSlotCaPort6_Object=MibTableColumn
dsMgcpSlotCaPort6=_DsMgcpSlotCaPort6_Object((1,3,6,1,4,1,6296,9,100,2,2,1,1,1,1,26),_DsMgcpSlotCaPort6_Type())
dsMgcpSlotCaPort6.setMaxAccess(_B)
if mibBuilder.loadTexts:dsMgcpSlotCaPort6.setStatus(_A)
_DsMgcpSlotCaPort7_Type=Integer32
_DsMgcpSlotCaPort7_Object=MibTableColumn
dsMgcpSlotCaPort7=_DsMgcpSlotCaPort7_Object((1,3,6,1,4,1,6296,9,100,2,2,1,1,1,1,27),_DsMgcpSlotCaPort7_Type())
dsMgcpSlotCaPort7.setMaxAccess(_B)
if mibBuilder.loadTexts:dsMgcpSlotCaPort7.setStatus(_A)
_DsMgcpSlotCaPort8_Type=Integer32
_DsMgcpSlotCaPort8_Object=MibTableColumn
dsMgcpSlotCaPort8=_DsMgcpSlotCaPort8_Object((1,3,6,1,4,1,6296,9,100,2,2,1,1,1,1,28),_DsMgcpSlotCaPort8_Type())
dsMgcpSlotCaPort8.setMaxAccess(_B)
if mibBuilder.loadTexts:dsMgcpSlotCaPort8.setStatus(_A)
class _DsMgcpSlotMgAddr_Type(DisplayString):defaultValue=OctetString(_D)
_DsMgcpSlotMgAddr_Type.__name__=_C
_DsMgcpSlotMgAddr_Object=MibTableColumn
dsMgcpSlotMgAddr=_DsMgcpSlotMgAddr_Object((1,3,6,1,4,1,6296,9,100,2,2,1,1,1,1,29),_DsMgcpSlotMgAddr_Type())
dsMgcpSlotMgAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:dsMgcpSlotMgAddr.setStatus(_A)
_DsMgcpSlotMgPort_Type=Integer32
_DsMgcpSlotMgPort_Object=MibTableColumn
dsMgcpSlotMgPort=_DsMgcpSlotMgPort_Object((1,3,6,1,4,1,6296,9,100,2,2,1,1,1,1,30),_DsMgcpSlotMgPort_Type())
dsMgcpSlotMgPort.setMaxAccess(_B)
if mibBuilder.loadTexts:dsMgcpSlotMgPort.setStatus(_A)
_DsAccGwyMgcpMonitor_ObjectIdentity=ObjectIdentity
dsAccGwyMgcpMonitor=_DsAccGwyMgcpMonitor_ObjectIdentity((1,3,6,1,4,1,6296,9,100,2,2,2))
_DsAccGwyMonitorMgcpSlot_ObjectIdentity=ObjectIdentity
dsAccGwyMonitorMgcpSlot=_DsAccGwyMonitorMgcpSlot_ObjectIdentity((1,3,6,1,4,1,6296,9,100,2,2,2,1))
_DsAccGwyMonitorMgcpSlotTable_Object=MibTable
dsAccGwyMonitorMgcpSlotTable=_DsAccGwyMonitorMgcpSlotTable_Object((1,3,6,1,4,1,6296,9,100,2,2,2,1,1))
if mibBuilder.loadTexts:dsAccGwyMonitorMgcpSlotTable.setStatus(_A)
_DsAccGwyMonitorMgcpSlotEntry_Object=MibTableRow
dsAccGwyMonitorMgcpSlotEntry=_DsAccGwyMonitorMgcpSlotEntry_Object((1,3,6,1,4,1,6296,9,100,2,2,2,1,1,1))
dsAccGwyMonitorMgcpSlotEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:dsAccGwyMonitorMgcpSlotEntry.setStatus(_A)
_DsMgcpMonitorMgcpStatus_Type=DisplayString
_DsMgcpMonitorMgcpStatus_Object=MibTableColumn
dsMgcpMonitorMgcpStatus=_DsMgcpMonitorMgcpStatus_Object((1,3,6,1,4,1,6296,9,100,2,2,2,1,1,1,1),_DsMgcpMonitorMgcpStatus_Type())
dsMgcpMonitorMgcpStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:dsMgcpMonitorMgcpStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'dasanAccessMib':dasanAccessMib,'dasanAccGatewayMIBObjects':dasanAccGatewayMIBObjects,'dsAccGwyMgcp':dsAccGwyMgcp,'dsAccGwyMgcpConfiguration':dsAccGwyMgcpConfiguration,'dsAccGwyConfigMgcpSlot':dsAccGwyConfigMgcpSlot,'dsAccGwyConfigMgcpSlotTable':dsAccGwyConfigMgcpSlotTable,'dsAccGwyConfigMgcpSlotEntry':dsAccGwyConfigMgcpSlotEntry,_F:dsMgcpSlotIndex,'dsMgcpSlotEncodePackageName':dsMgcpSlotEncodePackageName,'dsMgcpSlotRetransmitStartTimeout':dsMgcpSlotRetransmitStartTimeout,'dsMgcpSlotRetransmitMaxTimeout':dsMgcpSlotRetransmitMaxTimeout,'dsMgcpSlotRetransmitLongTimer':dsMgcpSlotRetransmitLongTimer,'dsMgcpSlotRetransmitMaxLifetime':dsMgcpSlotRetransmitMaxLifetime,'dsMgcpSlotRetransmitMax1':dsMgcpSlotRetransmitMax1,'dsMgcpSlotRetransmitMax2':dsMgcpSlotRetransmitMax2,'dsMgcpSlotRestartMaxwait':dsMgcpSlotRestartMaxwait,'dsMgcpSlotDisconnectInit':dsMgcpSlotDisconnectInit,'dsMgcpSlotDisconnectMin':dsMgcpSlotDisconnectMin,'dsMgcpSlotDisconnectMax':dsMgcpSlotDisconnectMax,'dsMgcpSlotCaAddr1':dsMgcpSlotCaAddr1,'dsMgcpSlotCaAddr2':dsMgcpSlotCaAddr2,'dsMgcpSlotCaAddr3':dsMgcpSlotCaAddr3,'dsMgcpSlotCaAddr4':dsMgcpSlotCaAddr4,'dsMgcpSlotCaAddr5':dsMgcpSlotCaAddr5,'dsMgcpSlotCaAddr6':dsMgcpSlotCaAddr6,'dsMgcpSlotCaAddr7':dsMgcpSlotCaAddr7,'dsMgcpSlotCaAddr8':dsMgcpSlotCaAddr8,'dsMgcpSlotCaPort1':dsMgcpSlotCaPort1,'dsMgcpSlotCaPort2':dsMgcpSlotCaPort2,'dsMgcpSlotCaPort3':dsMgcpSlotCaPort3,'dsMgcpSlotCaPort4':dsMgcpSlotCaPort4,'dsMgcpSlotCaPort5':dsMgcpSlotCaPort5,'dsMgcpSlotCaPort6':dsMgcpSlotCaPort6,'dsMgcpSlotCaPort7':dsMgcpSlotCaPort7,'dsMgcpSlotCaPort8':dsMgcpSlotCaPort8,'dsMgcpSlotMgAddr':dsMgcpSlotMgAddr,'dsMgcpSlotMgPort':dsMgcpSlotMgPort,'dsAccGwyMgcpMonitor':dsAccGwyMgcpMonitor,'dsAccGwyMonitorMgcpSlot':dsAccGwyMonitorMgcpSlot,'dsAccGwyMonitorMgcpSlotTable':dsAccGwyMonitorMgcpSlotTable,'dsAccGwyMonitorMgcpSlotEntry':dsAccGwyMonitorMgcpSlotEntry,'dsMgcpMonitorMgcpStatus':dsMgcpMonitorMgcpStatus})