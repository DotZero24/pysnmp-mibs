_O='mSerStatusGroup'
_N='mSerTermServerSerialRxBytes'
_M='mSerTermServerSerialRxPackets'
_L='mSerTermServerSerialTxBytes'
_K='mSerTermServerSerialTxPackets'
_J='mSerTermServerIpRxBytes'
_I='mSerTermServerIpRxPackets'
_H='mSerTermServerIpTxBytes'
_G='mSerTermServerIpTxPackets'
_F='mSerTermServerEnabled'
_E='mSerTermServerDescription'
_D='mSerTermServerSerialPort'
_C='read-only'
_B='MDS-SERIAL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mdsServices,=mibBuilder.importSymbols('MDS-ORBIT-SMI-MIB','mdsServices')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
mdsSerialMIB=ModuleIdentity((1,3,6,1,4,1,4130,10,3,2))
if mibBuilder.loadTexts:mdsSerialMIB.setRevisions(('2018-05-16 00:00','2014-05-12 00:00'))
_MSerMIBObjects_ObjectIdentity=ObjectIdentity
mSerMIBObjects=_MSerMIBObjects_ObjectIdentity((1,3,6,1,4,1,4130,10,3,2,1))
_MSerConfig_ObjectIdentity=ObjectIdentity
mSerConfig=_MSerConfig_ObjectIdentity((1,3,6,1,4,1,4130,10,3,2,1,1))
_MSerStatus_ObjectIdentity=ObjectIdentity
mSerStatus=_MSerStatus_ObjectIdentity((1,3,6,1,4,1,4130,10,3,2,1,2))
_MSerTermServerStatusTable_Object=MibTable
mSerTermServerStatusTable=_MSerTermServerStatusTable_Object((1,3,6,1,4,1,4130,10,3,2,1,2,1))
if mibBuilder.loadTexts:mSerTermServerStatusTable.setStatus(_A)
_MSerTermServerStatusEntry_Object=MibTableRow
mSerTermServerStatusEntry=_MSerTermServerStatusEntry_Object((1,3,6,1,4,1,4130,10,3,2,1,2,1,1))
mSerTermServerStatusEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:mSerTermServerStatusEntry.setStatus(_A)
_MSerTermServerSerialPort_Type=OctetString
_MSerTermServerSerialPort_Object=MibTableColumn
mSerTermServerSerialPort=_MSerTermServerSerialPort_Object((1,3,6,1,4,1,4130,10,3,2,1,2,1,1,1),_MSerTermServerSerialPort_Type())
mSerTermServerSerialPort.setMaxAccess(_C)
if mibBuilder.loadTexts:mSerTermServerSerialPort.setStatus(_A)
_MSerTermServerDescription_Type=OctetString
_MSerTermServerDescription_Object=MibTableColumn
mSerTermServerDescription=_MSerTermServerDescription_Object((1,3,6,1,4,1,4130,10,3,2,1,2,1,1,2),_MSerTermServerDescription_Type())
mSerTermServerDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:mSerTermServerDescription.setStatus(_A)
_MSerTermServerEnabled_Type=TruthValue
_MSerTermServerEnabled_Object=MibTableColumn
mSerTermServerEnabled=_MSerTermServerEnabled_Object((1,3,6,1,4,1,4130,10,3,2,1,2,1,1,3),_MSerTermServerEnabled_Type())
mSerTermServerEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:mSerTermServerEnabled.setStatus(_A)
_MSerTermServerIpTxPackets_Type=Unsigned32
_MSerTermServerIpTxPackets_Object=MibTableColumn
mSerTermServerIpTxPackets=_MSerTermServerIpTxPackets_Object((1,3,6,1,4,1,4130,10,3,2,1,2,1,1,6),_MSerTermServerIpTxPackets_Type())
mSerTermServerIpTxPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:mSerTermServerIpTxPackets.setStatus(_A)
_MSerTermServerIpTxBytes_Type=Unsigned32
_MSerTermServerIpTxBytes_Object=MibTableColumn
mSerTermServerIpTxBytes=_MSerTermServerIpTxBytes_Object((1,3,6,1,4,1,4130,10,3,2,1,2,1,1,7),_MSerTermServerIpTxBytes_Type())
mSerTermServerIpTxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:mSerTermServerIpTxBytes.setStatus(_A)
_MSerTermServerIpRxPackets_Type=Unsigned32
_MSerTermServerIpRxPackets_Object=MibTableColumn
mSerTermServerIpRxPackets=_MSerTermServerIpRxPackets_Object((1,3,6,1,4,1,4130,10,3,2,1,2,1,1,8),_MSerTermServerIpRxPackets_Type())
mSerTermServerIpRxPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:mSerTermServerIpRxPackets.setStatus(_A)
_MSerTermServerIpRxBytes_Type=Unsigned32
_MSerTermServerIpRxBytes_Object=MibTableColumn
mSerTermServerIpRxBytes=_MSerTermServerIpRxBytes_Object((1,3,6,1,4,1,4130,10,3,2,1,2,1,1,9),_MSerTermServerIpRxBytes_Type())
mSerTermServerIpRxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:mSerTermServerIpRxBytes.setStatus(_A)
_MSerTermServerSerialTxPackets_Type=Unsigned32
_MSerTermServerSerialTxPackets_Object=MibTableColumn
mSerTermServerSerialTxPackets=_MSerTermServerSerialTxPackets_Object((1,3,6,1,4,1,4130,10,3,2,1,2,1,1,10),_MSerTermServerSerialTxPackets_Type())
mSerTermServerSerialTxPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:mSerTermServerSerialTxPackets.setStatus(_A)
_MSerTermServerSerialTxBytes_Type=Unsigned32
_MSerTermServerSerialTxBytes_Object=MibTableColumn
mSerTermServerSerialTxBytes=_MSerTermServerSerialTxBytes_Object((1,3,6,1,4,1,4130,10,3,2,1,2,1,1,11),_MSerTermServerSerialTxBytes_Type())
mSerTermServerSerialTxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:mSerTermServerSerialTxBytes.setStatus(_A)
_MSerTermServerSerialRxPackets_Type=Unsigned32
_MSerTermServerSerialRxPackets_Object=MibTableColumn
mSerTermServerSerialRxPackets=_MSerTermServerSerialRxPackets_Object((1,3,6,1,4,1,4130,10,3,2,1,2,1,1,12),_MSerTermServerSerialRxPackets_Type())
mSerTermServerSerialRxPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:mSerTermServerSerialRxPackets.setStatus(_A)
_MSerTermServerSerialRxBytes_Type=Unsigned32
_MSerTermServerSerialRxBytes_Object=MibTableColumn
mSerTermServerSerialRxBytes=_MSerTermServerSerialRxBytes_Object((1,3,6,1,4,1,4130,10,3,2,1,2,1,1,13),_MSerTermServerSerialRxBytes_Type())
mSerTermServerSerialRxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:mSerTermServerSerialRxBytes.setStatus(_A)
_MdsSerMIBConformance_ObjectIdentity=ObjectIdentity
mdsSerMIBConformance=_MdsSerMIBConformance_ObjectIdentity((1,3,6,1,4,1,4130,10,3,2,3))
_MdsSerMIBCompliances_ObjectIdentity=ObjectIdentity
mdsSerMIBCompliances=_MdsSerMIBCompliances_ObjectIdentity((1,3,6,1,4,1,4130,10,3,2,3,1))
_MdsSerMIBGroups_ObjectIdentity=ObjectIdentity
mdsSerMIBGroups=_MdsSerMIBGroups_ObjectIdentity((1,3,6,1,4,1,4130,10,3,2,3,2))
mSerStatusGroup=ObjectGroup((1,3,6,1,4,1,4130,10,3,2,3,2,1))
mSerStatusGroup.setObjects(*((_B,_D),(_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:mSerStatusGroup.setStatus(_A)
mSerCompliance=ModuleCompliance((1,3,6,1,4,1,4130,10,3,2,3,1,1))
mSerCompliance.setObjects((_B,_O))
if mibBuilder.loadTexts:mSerCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'mdsSerialMIB':mdsSerialMIB,'mSerMIBObjects':mSerMIBObjects,'mSerConfig':mSerConfig,'mSerStatus':mSerStatus,'mSerTermServerStatusTable':mSerTermServerStatusTable,'mSerTermServerStatusEntry':mSerTermServerStatusEntry,_D:mSerTermServerSerialPort,_E:mSerTermServerDescription,_F:mSerTermServerEnabled,_G:mSerTermServerIpTxPackets,_H:mSerTermServerIpTxBytes,_I:mSerTermServerIpRxPackets,_J:mSerTermServerIpRxBytes,_K:mSerTermServerSerialTxPackets,_L:mSerTermServerSerialTxBytes,_M:mSerTermServerSerialRxPackets,_N:mSerTermServerSerialRxBytes,'mdsSerMIBConformance':mdsSerMIBConformance,'mdsSerMIBCompliances':mdsSerMIBCompliances,'mSerCompliance':mSerCompliance,'mdsSerMIBGroups':mdsSerMIBGroups,_O:mSerStatusGroup})