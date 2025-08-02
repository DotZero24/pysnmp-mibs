_J='not-accessible'
_I='eltMesIssDhcpSrvHostInterfaceOptType'
_H='DisplayString'
_G='Integer32'
_F='eltMesIssDhcpSrvHostInterfaceIfIndex'
_E='dhcpSrvSubnetPoolIndex'
_D='ARICENT-DHCP-SERVER-MIB'
_C='ELTEX-MES-ISS-DHCP-SRV-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dhcpSrvSubnetPoolIndex,=mibBuilder.importSymbols(_D,_E)
eltMesIss,=mibBuilder.importSymbols('ELTEX-MES-ISS-MIB','eltMesIss')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','RowStatus','TextualConvention')
eltMesIssDhcpSrvMIB=ModuleIdentity((1,3,6,1,4,1,35265,1,139,33))
if mibBuilder.loadTexts:eltMesIssDhcpSrvMIB.setRevisions(('2023-04-10 00:00',))
_EltMesIssDhcpSrvObjects_ObjectIdentity=ObjectIdentity
eltMesIssDhcpSrvObjects=_EltMesIssDhcpSrvObjects_ObjectIdentity((1,3,6,1,4,1,35265,1,139,33,1))
_EltMesIssDhcpSrvGlobals_ObjectIdentity=ObjectIdentity
eltMesIssDhcpSrvGlobals=_EltMesIssDhcpSrvGlobals_ObjectIdentity((1,3,6,1,4,1,35265,1,139,33,1,1))
_EltMesIssDhcpSrvConfig_ObjectIdentity=ObjectIdentity
eltMesIssDhcpSrvConfig=_EltMesIssDhcpSrvConfig_ObjectIdentity((1,3,6,1,4,1,35265,1,139,33,1,2))
_EltMesIssDhcpSrvHostInterfaceOptTable_Object=MibTable
eltMesIssDhcpSrvHostInterfaceOptTable=_EltMesIssDhcpSrvHostInterfaceOptTable_Object((1,3,6,1,4,1,35265,1,139,33,1,2,1))
if mibBuilder.loadTexts:eltMesIssDhcpSrvHostInterfaceOptTable.setStatus(_A)
_EltMesIssDhcpSrvHostInterfaceOptEntry_Object=MibTableRow
eltMesIssDhcpSrvHostInterfaceOptEntry=_EltMesIssDhcpSrvHostInterfaceOptEntry_Object((1,3,6,1,4,1,35265,1,139,33,1,2,1,1))
eltMesIssDhcpSrvHostInterfaceOptEntry.setIndexNames((0,_C,_F),(0,_D,_E),(0,_C,_I))
if mibBuilder.loadTexts:eltMesIssDhcpSrvHostInterfaceOptEntry.setStatus(_A)
_EltMesIssDhcpSrvHostInterfaceIfIndex_Type=InterfaceIndex
_EltMesIssDhcpSrvHostInterfaceIfIndex_Object=MibTableColumn
eltMesIssDhcpSrvHostInterfaceIfIndex=_EltMesIssDhcpSrvHostInterfaceIfIndex_Object((1,3,6,1,4,1,35265,1,139,33,1,2,1,1,1),_EltMesIssDhcpSrvHostInterfaceIfIndex_Type())
eltMesIssDhcpSrvHostInterfaceIfIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:eltMesIssDhcpSrvHostInterfaceIfIndex.setStatus(_A)
class _EltMesIssDhcpSrvHostInterfaceOptType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_EltMesIssDhcpSrvHostInterfaceOptType_Type.__name__=_G
_EltMesIssDhcpSrvHostInterfaceOptType_Object=MibTableColumn
eltMesIssDhcpSrvHostInterfaceOptType=_EltMesIssDhcpSrvHostInterfaceOptType_Object((1,3,6,1,4,1,35265,1,139,33,1,2,1,1,2),_EltMesIssDhcpSrvHostInterfaceOptType_Type())
eltMesIssDhcpSrvHostInterfaceOptType.setMaxAccess(_J)
if mibBuilder.loadTexts:eltMesIssDhcpSrvHostInterfaceOptType.setStatus(_A)
_EltMesIssDhcpSrvHostInterfaceOptLen_Type=Integer32
_EltMesIssDhcpSrvHostInterfaceOptLen_Object=MibTableColumn
eltMesIssDhcpSrvHostInterfaceOptLen=_EltMesIssDhcpSrvHostInterfaceOptLen_Object((1,3,6,1,4,1,35265,1,139,33,1,2,1,1,3),_EltMesIssDhcpSrvHostInterfaceOptLen_Type())
eltMesIssDhcpSrvHostInterfaceOptLen.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssDhcpSrvHostInterfaceOptLen.setStatus(_A)
_EltMesIssDhcpSrvHostInterfaceOptVal_Type=OctetString
_EltMesIssDhcpSrvHostInterfaceOptVal_Object=MibTableColumn
eltMesIssDhcpSrvHostInterfaceOptVal=_EltMesIssDhcpSrvHostInterfaceOptVal_Object((1,3,6,1,4,1,35265,1,139,33,1,2,1,1,4),_EltMesIssDhcpSrvHostInterfaceOptVal_Type())
eltMesIssDhcpSrvHostInterfaceOptVal.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssDhcpSrvHostInterfaceOptVal.setStatus(_A)
_EltMesIssDhcpSrvHostInterfaceOptRowStatus_Type=RowStatus
_EltMesIssDhcpSrvHostInterfaceOptRowStatus_Object=MibTableColumn
eltMesIssDhcpSrvHostInterfaceOptRowStatus=_EltMesIssDhcpSrvHostInterfaceOptRowStatus_Object((1,3,6,1,4,1,35265,1,139,33,1,2,1,1,5),_EltMesIssDhcpSrvHostInterfaceOptRowStatus_Type())
eltMesIssDhcpSrvHostInterfaceOptRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssDhcpSrvHostInterfaceOptRowStatus.setStatus(_A)
_EltMesIssDhcpSrvHostInterfaceConfigTable_Object=MibTable
eltMesIssDhcpSrvHostInterfaceConfigTable=_EltMesIssDhcpSrvHostInterfaceConfigTable_Object((1,3,6,1,4,1,35265,1,139,33,1,2,2))
if mibBuilder.loadTexts:eltMesIssDhcpSrvHostInterfaceConfigTable.setStatus(_A)
_EltMesIssDhcpSrvHostInterfaceConfigEntry_Object=MibTableRow
eltMesIssDhcpSrvHostInterfaceConfigEntry=_EltMesIssDhcpSrvHostInterfaceConfigEntry_Object((1,3,6,1,4,1,35265,1,139,33,1,2,2,1))
eltMesIssDhcpSrvHostInterfaceConfigEntry.setIndexNames((0,_C,_F),(0,_D,_E))
if mibBuilder.loadTexts:eltMesIssDhcpSrvHostInterfaceConfigEntry.setStatus(_A)
_EltMesIssDhcpSrvHostInterfaceIpAddress_Type=IpAddress
_EltMesIssDhcpSrvHostInterfaceIpAddress_Object=MibTableColumn
eltMesIssDhcpSrvHostInterfaceIpAddress=_EltMesIssDhcpSrvHostInterfaceIpAddress_Object((1,3,6,1,4,1,35265,1,139,33,1,2,2,1,1),_EltMesIssDhcpSrvHostInterfaceIpAddress_Type())
eltMesIssDhcpSrvHostInterfaceIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssDhcpSrvHostInterfaceIpAddress.setStatus(_A)
_EltMesIssDhcpSrvHostInterfacePoolName_Type=Integer32
_EltMesIssDhcpSrvHostInterfacePoolName_Object=MibTableColumn
eltMesIssDhcpSrvHostInterfacePoolName=_EltMesIssDhcpSrvHostInterfacePoolName_Object((1,3,6,1,4,1,35265,1,139,33,1,2,2,1,2),_EltMesIssDhcpSrvHostInterfacePoolName_Type())
eltMesIssDhcpSrvHostInterfacePoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssDhcpSrvHostInterfacePoolName.setStatus(_A)
class _EltMesIssDhcpSrvHostInterfaceBootFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_EltMesIssDhcpSrvHostInterfaceBootFileName_Type.__name__=_H
_EltMesIssDhcpSrvHostInterfaceBootFileName_Object=MibTableColumn
eltMesIssDhcpSrvHostInterfaceBootFileName=_EltMesIssDhcpSrvHostInterfaceBootFileName_Object((1,3,6,1,4,1,35265,1,139,33,1,2,2,1,3),_EltMesIssDhcpSrvHostInterfaceBootFileName_Type())
eltMesIssDhcpSrvHostInterfaceBootFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssDhcpSrvHostInterfaceBootFileName.setStatus(_A)
_EltMesIssDhcpSrvHostInterfaceBootServerAddress_Type=IpAddress
_EltMesIssDhcpSrvHostInterfaceBootServerAddress_Object=MibTableColumn
eltMesIssDhcpSrvHostInterfaceBootServerAddress=_EltMesIssDhcpSrvHostInterfaceBootServerAddress_Object((1,3,6,1,4,1,35265,1,139,33,1,2,2,1,4),_EltMesIssDhcpSrvHostInterfaceBootServerAddress_Type())
eltMesIssDhcpSrvHostInterfaceBootServerAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssDhcpSrvHostInterfaceBootServerAddress.setStatus(_A)
_EltMesIssDhcpSrvHostInterfaceConfigRowStatus_Type=RowStatus
_EltMesIssDhcpSrvHostInterfaceConfigRowStatus_Object=MibTableColumn
eltMesIssDhcpSrvHostInterfaceConfigRowStatus=_EltMesIssDhcpSrvHostInterfaceConfigRowStatus_Object((1,3,6,1,4,1,35265,1,139,33,1,2,2,1,5),_EltMesIssDhcpSrvHostInterfaceConfigRowStatus_Type())
eltMesIssDhcpSrvHostInterfaceConfigRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssDhcpSrvHostInterfaceConfigRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'eltMesIssDhcpSrvMIB':eltMesIssDhcpSrvMIB,'eltMesIssDhcpSrvObjects':eltMesIssDhcpSrvObjects,'eltMesIssDhcpSrvGlobals':eltMesIssDhcpSrvGlobals,'eltMesIssDhcpSrvConfig':eltMesIssDhcpSrvConfig,'eltMesIssDhcpSrvHostInterfaceOptTable':eltMesIssDhcpSrvHostInterfaceOptTable,'eltMesIssDhcpSrvHostInterfaceOptEntry':eltMesIssDhcpSrvHostInterfaceOptEntry,_F:eltMesIssDhcpSrvHostInterfaceIfIndex,_I:eltMesIssDhcpSrvHostInterfaceOptType,'eltMesIssDhcpSrvHostInterfaceOptLen':eltMesIssDhcpSrvHostInterfaceOptLen,'eltMesIssDhcpSrvHostInterfaceOptVal':eltMesIssDhcpSrvHostInterfaceOptVal,'eltMesIssDhcpSrvHostInterfaceOptRowStatus':eltMesIssDhcpSrvHostInterfaceOptRowStatus,'eltMesIssDhcpSrvHostInterfaceConfigTable':eltMesIssDhcpSrvHostInterfaceConfigTable,'eltMesIssDhcpSrvHostInterfaceConfigEntry':eltMesIssDhcpSrvHostInterfaceConfigEntry,'eltMesIssDhcpSrvHostInterfaceIpAddress':eltMesIssDhcpSrvHostInterfaceIpAddress,'eltMesIssDhcpSrvHostInterfacePoolName':eltMesIssDhcpSrvHostInterfacePoolName,'eltMesIssDhcpSrvHostInterfaceBootFileName':eltMesIssDhcpSrvHostInterfaceBootFileName,'eltMesIssDhcpSrvHostInterfaceBootServerAddress':eltMesIssDhcpSrvHostInterfaceBootServerAddress,'eltMesIssDhcpSrvHostInterfaceConfigRowStatus':eltMesIssDhcpSrvHostInterfaceConfigRowStatus})