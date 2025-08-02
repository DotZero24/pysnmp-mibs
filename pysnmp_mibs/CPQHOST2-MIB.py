_H='cpqHoClientIndex'
_G='CPQHOST2-MIB'
_F='NotificationType'
_E='Integer32'
_D='DisplayString'
_C='OctetString'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols('SNMPv2-MIB','sysName')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier',_F,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_F,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
_Compaq_ObjectIdentity=ObjectIdentity
compaq=_Compaq_ObjectIdentity((1,3,6,1,4,1,232))
_CpqHostOs_ObjectIdentity=ObjectIdentity
cpqHostOs=_CpqHostOs_ObjectIdentity((1,3,6,1,4,1,232,11))
_CpqHoComponent_ObjectIdentity=ObjectIdentity
cpqHoComponent=_CpqHoComponent_ObjectIdentity((1,3,6,1,4,1,232,11,2))
_CpqHoClients_ObjectIdentity=ObjectIdentity
cpqHoClients=_CpqHoClients_ObjectIdentity((1,3,6,1,4,1,232,11,2,12))
class _CpqHoClientLastModified_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(7,7));fixedLength=7
_CpqHoClientLastModified_Type.__name__=_C
_CpqHoClientLastModified_Object=MibScalar
cpqHoClientLastModified=_CpqHoClientLastModified_Object((1,3,6,1,4,1,232,11,2,12,1),_CpqHoClientLastModified_Type())
cpqHoClientLastModified.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoClientLastModified.setStatus(_A)
class _CpqHoClientDelete_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_CpqHoClientDelete_Type.__name__=_D
_CpqHoClientDelete_Object=MibScalar
cpqHoClientDelete=_CpqHoClientDelete_Object((1,3,6,1,4,1,232,11,2,12,2),_CpqHoClientDelete_Type())
cpqHoClientDelete.setMaxAccess('read-write')
if mibBuilder.loadTexts:cpqHoClientDelete.setStatus(_A)
_CpqHoClientTable_Object=MibTable
cpqHoClientTable=_CpqHoClientTable_Object((1,3,6,1,4,1,232,11,2,12,3))
if mibBuilder.loadTexts:cpqHoClientTable.setStatus(_A)
_CpqHoClientEntry_Object=MibTableRow
cpqHoClientEntry=_CpqHoClientEntry_Object((1,3,6,1,4,1,232,11,2,12,3,1))
cpqHoClientEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:cpqHoClientEntry.setStatus(_A)
class _CpqHoClientIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqHoClientIndex_Type.__name__=_E
_CpqHoClientIndex_Object=MibTableColumn
cpqHoClientIndex=_CpqHoClientIndex_Object((1,3,6,1,4,1,232,11,2,12,3,1,1),_CpqHoClientIndex_Type())
cpqHoClientIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoClientIndex.setStatus(_A)
class _CpqHoClientName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_CpqHoClientName_Type.__name__=_D
_CpqHoClientName_Object=MibTableColumn
cpqHoClientName=_CpqHoClientName_Object((1,3,6,1,4,1,232,11,2,12,3,1,2),_CpqHoClientName_Type())
cpqHoClientName.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoClientName.setStatus(_A)
class _CpqHoClientIpxAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(20,20));fixedLength=20
_CpqHoClientIpxAddress_Type.__name__=_C
_CpqHoClientIpxAddress_Object=MibTableColumn
cpqHoClientIpxAddress=_CpqHoClientIpxAddress_Object((1,3,6,1,4,1,232,11,2,12,3,1,3),_CpqHoClientIpxAddress_Type())
cpqHoClientIpxAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoClientIpxAddress.setStatus(_A)
_CpqHoClientIpAddress_Type=IpAddress
_CpqHoClientIpAddress_Object=MibTableColumn
cpqHoClientIpAddress=_CpqHoClientIpAddress_Object((1,3,6,1,4,1,232,11,2,12,3,1,4),_CpqHoClientIpAddress_Type())
cpqHoClientIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoClientIpAddress.setStatus(_A)
class _CpqHoClientCommunity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,48))
_CpqHoClientCommunity_Type.__name__=_D
_CpqHoClientCommunity_Object=MibTableColumn
cpqHoClientCommunity=_CpqHoClientCommunity_Object((1,3,6,1,4,1,232,11,2,12,3,1,5),_CpqHoClientCommunity_Type())
cpqHoClientCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoClientCommunity.setStatus(_A)
class _CpqHoClientID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_CpqHoClientID_Type.__name__=_C
_CpqHoClientID_Object=MibTableColumn
cpqHoClientID=_CpqHoClientID_Object((1,3,6,1,4,1,232,11,2,12,3,1,6),_CpqHoClientID_Type())
cpqHoClientID.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoClientID.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'compaq':compaq,'cpqHostOs':cpqHostOs,'cpqHoComponent':cpqHoComponent,'cpqHoClients':cpqHoClients,'cpqHoClientLastModified':cpqHoClientLastModified,'cpqHoClientDelete':cpqHoClientDelete,'cpqHoClientTable':cpqHoClientTable,'cpqHoClientEntry':cpqHoClientEntry,_H:cpqHoClientIndex,'cpqHoClientName':cpqHoClientName,'cpqHoClientIpxAddress':cpqHoClientIpxAddress,'cpqHoClientIpAddress':cpqHoClientIpAddress,'cpqHoClientCommunity':cpqHoClientCommunity,'cpqHoClientID':cpqHoClientID})