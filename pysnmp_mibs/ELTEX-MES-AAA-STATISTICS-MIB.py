_I='eltRadiusServerAcctPortNumber'
_H='eltRadiusServerAuthPortNumber'
_G='eltRadiusServerAddress'
_F='eltRadiusServerAddressType'
_E='read-only'
_D='Integer32'
_C='read-write'
_B='ELTEX-MES-AAA-STATISTICS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltMesAAAStatMIB,=mibBuilder.importSymbols('ELTEX-MES-MNG-MIB','eltMesAAAStatMIB')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
_EltRadiusServerStatusTable_Object=MibTable
eltRadiusServerStatusTable=_EltRadiusServerStatusTable_Object((1,3,6,1,4,1,35265,1,23,1,3,21))
if mibBuilder.loadTexts:eltRadiusServerStatusTable.setStatus(_A)
_EltRadiusServerStatusEntry_Object=MibTableRow
eltRadiusServerStatusEntry=_EltRadiusServerStatusEntry_Object((1,3,6,1,4,1,35265,1,23,1,3,21,1))
eltRadiusServerStatusEntry.setIndexNames((0,_B,_F),(0,_B,_G),(0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:eltRadiusServerStatusEntry.setStatus(_A)
_EltRadiusServerAddressType_Type=InetAddressType
_EltRadiusServerAddressType_Object=MibTableColumn
eltRadiusServerAddressType=_EltRadiusServerAddressType_Object((1,3,6,1,4,1,35265,1,23,1,3,21,1,1),_EltRadiusServerAddressType_Type())
eltRadiusServerAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:eltRadiusServerAddressType.setStatus(_A)
_EltRadiusServerAddress_Type=InetAddress
_EltRadiusServerAddress_Object=MibTableColumn
eltRadiusServerAddress=_EltRadiusServerAddress_Object((1,3,6,1,4,1,35265,1,23,1,3,21,1,2),_EltRadiusServerAddress_Type())
eltRadiusServerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:eltRadiusServerAddress.setStatus(_A)
class _EltRadiusServerAuthPortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_EltRadiusServerAuthPortNumber_Type.__name__=_D
_EltRadiusServerAuthPortNumber_Object=MibTableColumn
eltRadiusServerAuthPortNumber=_EltRadiusServerAuthPortNumber_Object((1,3,6,1,4,1,35265,1,23,1,3,21,1,3),_EltRadiusServerAuthPortNumber_Type())
eltRadiusServerAuthPortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:eltRadiusServerAuthPortNumber.setStatus(_A)
class _EltRadiusServerAcctPortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_EltRadiusServerAcctPortNumber_Type.__name__=_D
_EltRadiusServerAcctPortNumber_Object=MibTableColumn
eltRadiusServerAcctPortNumber=_EltRadiusServerAcctPortNumber_Object((1,3,6,1,4,1,35265,1,23,1,3,21,1,4),_EltRadiusServerAcctPortNumber_Type())
eltRadiusServerAcctPortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:eltRadiusServerAcctPortNumber.setStatus(_A)
_EltRadiusServerAuthClientTimeouts_Type=Unsigned32
_EltRadiusServerAuthClientTimeouts_Object=MibTableColumn
eltRadiusServerAuthClientTimeouts=_EltRadiusServerAuthClientTimeouts_Object((1,3,6,1,4,1,35265,1,23,1,3,21,1,5),_EltRadiusServerAuthClientTimeouts_Type())
eltRadiusServerAuthClientTimeouts.setMaxAccess(_E)
if mibBuilder.loadTexts:eltRadiusServerAuthClientTimeouts.setStatus(_A)
_EltRadiusServerDeadStatus_Type=TruthValue
_EltRadiusServerDeadStatus_Object=MibTableColumn
eltRadiusServerDeadStatus=_EltRadiusServerDeadStatus_Object((1,3,6,1,4,1,35265,1,23,1,3,21,1,6),_EltRadiusServerDeadStatus_Type())
eltRadiusServerDeadStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:eltRadiusServerDeadStatus.setStatus(_A)
_EltRadiusServerRemainDeadTime_Type=Unsigned32
_EltRadiusServerRemainDeadTime_Object=MibTableColumn
eltRadiusServerRemainDeadTime=_EltRadiusServerRemainDeadTime_Object((1,3,6,1,4,1,35265,1,23,1,3,21,1,7),_EltRadiusServerRemainDeadTime_Type())
eltRadiusServerRemainDeadTime.setMaxAccess(_E)
if mibBuilder.loadTexts:eltRadiusServerRemainDeadTime.setStatus(_A)
class _EltRadiusServerStatusReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_EltRadiusServerStatusReset_Type.__name__=_D
_EltRadiusServerStatusReset_Object=MibScalar
eltRadiusServerStatusReset=_EltRadiusServerStatusReset_Object((1,3,6,1,4,1,35265,1,23,1,3,22),_EltRadiusServerStatusReset_Type())
eltRadiusServerStatusReset.setMaxAccess(_C)
if mibBuilder.loadTexts:eltRadiusServerStatusReset.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'eltRadiusServerStatusTable':eltRadiusServerStatusTable,'eltRadiusServerStatusEntry':eltRadiusServerStatusEntry,_F:eltRadiusServerAddressType,_G:eltRadiusServerAddress,_H:eltRadiusServerAuthPortNumber,_I:eltRadiusServerAcctPortNumber,'eltRadiusServerAuthClientTimeouts':eltRadiusServerAuthClientTimeouts,'eltRadiusServerDeadStatus':eltRadiusServerDeadStatus,'eltRadiusServerRemainDeadTime':eltRadiusServerRemainDeadTime,'eltRadiusServerStatusReset':eltRadiusServerStatusReset})